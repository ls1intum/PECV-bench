from typing import Dict, List
from uuid import uuid4
from langchain_core.runnables import RunnableParallel, RunnableLambda  # type: ignore[import]

try:  # pragma: no cover - optional dependency
    from langfuse.callback import CallbackHandler  # type: ignore[import]
except ImportError:  # pragma: no cover - optional dependency
    CallbackHandler = None  # type: ignore[assignment]

from ..settings import settings
from ..models import init_chat_model

from .models import (
    Metadata,
    ConsistencyCheckRequest,
    ConsistencyCheckResponse,
    ConsistencyIssue,
)
from .checker.structural import init_structural_checker
from .checker.semantic import init_semantic_checker


class ConsistencyCheck:

    def __init__(self, model: str, reasoning_effort: str = "medium"):
        self.model = init_chat_model(
            model,
            reasoning_effort=reasoning_effort,
        )

    def check(self, request: ConsistencyCheckRequest) -> ConsistencyCheckResponse:
        trace_id = uuid4()

        input_data = {
            "problem_statement": request.problem_statement,
            "programming_language": request.programming_language,
            "template_repository": [
                {"path": file.path, "content": file.content}
                for file in request.template_repository.files
            ],
        }

        # Add optional repositories if they exist
        if request.solution_repository:
            input_data["solution_repository"] = [
                {"path": file.path, "content": file.content}
                for file in request.solution_repository.files
            ]

        if request.test_repository:
            input_data["test_repository"] = [
                {"path": file.path, "content": file.content}
                for file in request.test_repository.files
            ]

        structural_checker = init_structural_checker(self.model)
        semantic_checker = init_semantic_checker(self.model)

        def merge_issues(results: Dict) -> List[ConsistencyIssue]:
            """Merge issues from results."""
            return [issue for result in results.values() for issue in result.issues]

        merge = RunnableLambda(merge_issues, name="merge_issues")

        callbacks = []
        if CallbackHandler is not None and getattr(
            settings, "is_langfuse_enabled", False
        ):
            callbacks.append(CallbackHandler())

        checker = (
            RunnableParallel(
                {
                    "structural": structural_checker,
                    "semantic": semantic_checker,
                }
            )
            | merge
        ).with_config(
            {
                "callbacks": callbacks,
                "run_name": "consistency_check",
                "run_id": trace_id,
            }
        )

        issues = checker.invoke(input_data)

        return ConsistencyCheckResponse(
            issues=issues,
            metadata=Metadata(trace_id=str(trace_id)),
        )
