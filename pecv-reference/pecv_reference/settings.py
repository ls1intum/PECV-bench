from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(override=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    # Model to use prefixed by provider, i.e. "openai:o4-mini"
    MODEL_NAME: str = ""

    # OpenRouter
    OPENROUTER_API_KEY: str = ""

    # OpenWebUI
    OPENWEBUI_API_KEY: str = ""
    OPENWEBUI_BASE_URL: str = ""

    LANGFUSE_PUBLIC_KEY: str = ""
    LANGFUSE_SECRET_KEY: str = ""

    @property
    def is_langfuse_enabled(self) -> bool:
        return bool(self.LANGFUSE_PUBLIC_KEY and self.LANGFUSE_SECRET_KEY)

    LANGSMITH_TRACING: bool = True
    LANGSMITH_API_KEY: str = "lsv2_pt_your-api-key"
    LANGCHAIN_PROJECT: str = "pecv-reference"

    @property
    def is_langsmith_enabled(self) -> bool:
        return bool(self.LANGSMITH_TRACING and self.LANGSMITH_API_KEY)


settings = Settings()
