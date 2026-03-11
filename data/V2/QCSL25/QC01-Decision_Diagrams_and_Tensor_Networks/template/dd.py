################################################################################
# Essential data structures to work with decision diagrams (DDs)               #
#                                                                              #
# This includes:                                                               #
# - DD: A data structure for representing DDs.                                 #
# - DDNode: A data structure for representing individual nodes in a DD.        #
# - UniqueTable: A simple unique table implementation.                         #
# - DDOperation: An Enum of different operations that can be applied to DDs.   #
# - ComputeTable: A simple compute table implementation.                       #
#                                                                              #
# Make sure to read the docstrings of the individual classes and make yourself #
# familiar with the code as it will be used throughout the exercise.           #
#                                                                              #
################################################################################

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


@dataclass
class DD:
    """A data structure for representing a decision diagram (DD).

    DDs are weighted directed acyclic graphs (DAGs) that represent complex
    vectors and matrices. They are used to represent quantum states and
    operations in a compact way.

    To this end, they are recursively defined as a collection of nodes that are
    interlinked with each other (with each link/edge being assigned a complex
    weight).

            | weight
          ( p )
         / ... \\
       other (sub-)DDs

    Attributes:
        node: The actual DD node
        weight: The edge weight associated to the edge pointing to the node.
    """

    node: DDNode  # forward reference
    weight: np.complex128

    def __hash__(self) -> int:
        """
        Defines a unique hash for the DD class.

        This is essential to quickly determine if a DD already exists.
        """
        return hash((id(self.node), self.weight))

    def __eq__(self, other: DD) -> bool:
        """
        Defines the equality operator for the DD class.

        DDs are considered equal when they have the same node and roughly the
        same weight (up to a small epsilon).
        """
        return id(self.node) == id(other.node) and np.isclose(self.weight, other.weight)

    def is_terminal(self) -> bool:
        """Returns True if the DD is a terminal node, False otherwise."""
        return self.node.is_terminal()

    def is_zero_terminal(self) -> bool:
        """Returns True if the DD is a zero terminal, False otherwise."""
        return self.is_terminal() and self.weight == 0

    def is_one_terminal(self) -> bool:
        """Returns True if the DD is a one terminal, False otherwise."""
        return self.is_terminal() and self.weight == 1

    def is_vector(self) -> bool:
        """Returns True if the DD is a vector, False otherwise."""
        return len(self.node.successors) == 2

    def is_matrix(self) -> bool:
        """Returns True if the DD is a matrix, False otherwise."""
        return len(self.node.successors) == 4

    def num_qubits(self) -> int:
        """Returns the number of qubits in the DD."""
        return self.node.v + 1


@dataclass
class DDNode:
    """A class for representing individual nodes in a decision diagram (DD).

    The nodes of the graph are labeled with integers (corresponding to qubit
    indices), and each node has a certain number of outgoing edges. The number
    of outgoing edges is determined by the type of representation (vector or
    matrix). Each successor can be considered a DD itself, where the edge to the
    successor is labeled with a complex-valued weight.

    For vector representations, there are exactly two outgoing edges per node;
    representing the 0-successor and the 1-successor.
                  | weight
                 (v)                = [    ...    |    ...    ]^T
                /   \\                 0-successor  1-successor
     0-successor    1-successor
          ----------------- next level
          w0 |       | w1
           (v-1)   (v-1)
           /  \\   /  \\


    For matrix representations,there are four outgoing edges per node;
    representing the four quadrants of the matrix at the current level with
        0 denoting the upper left quadrant,
        1 denoting the upper right quadrant,
        2 denoting the lower left quadrant, and
        3 denoting the lower right quadrant.

                  | weight          U00 | U01
                 (v)            =   ---------
               / | | \\              U10 | U11
             /  /  \\  \\
            00 01  10 11

    Note that the convention is to store the most significant qubit at the top
    of the graph, and the least significant qubit at the bottom of the graph.
    This means that in an n-qubit system, the root node is labeled with n-1,
    and the last level of nodes before the terminal nodes is labeled with 0.

    Attributes:
        v: The index of the qubit associated with this node. If the node is a
        terminal node, this is supposed to be -1.
        successors: The list of successor DDs..
    """

    v: int
    successors: list[DD]

    def __hash__(self) -> int:
        """
        Defines a unique hash for the DDNode class.

        This is essential to quickly determine if a node already exists.
        """
        return hash((self.v, tuple(hash(x) for x in self.successors)))

    def __eq__(self, other: DDNode) -> bool:
        """
        Defines the equality operator for the DDNode class.

        Nodes are considered equal they operate on the same level and have the
        same successors.
        """
        return self.v == other.v and self.successors == other.successors

    def is_terminal(self) -> bool:
        """Returns True if the node is a terminal node, False otherwise."""
        return self.v == -1


@dataclass
class UniqueTable:
    """A simple unique table implementation.

    This class is used to keep track of unique nodes in the graph. It is really
    just a dictionary that maps a hash of a node to the node itself. It uses
    linear probing to resolve collisions. This is not a very efficient
    implementation, but it is sufficient for our purposes.

    Attributes:
        table: The dictionary that maps a hash of a node to the node itself.
    """

    table: dict[int, DDNode]

    def __init__(self) -> None:
        """Initializes an empty unique table."""
        self.table = {}

    def lookup(self, node: DDNode) -> DDNode:
        """Looks up a node in the unique table.

        Args:
            node: The node to look up.

        Returns:
            The node if it is in the table, or the node itself if it is not.
        """
        key = hash(node)
        while key in self.table and self.table[key] != node:
            key += 1

        if key not in self.table:
            self.table[key] = node

        return self.table[key]

    def clear(self) -> None:
        """Clears the unique table."""
        self.table.clear()


class DDOperation(Enum):
    """An enumeration of the different operations that can be applied to a DD."""

    ADDITION = 1
    MULTIPLICATION = 2


@dataclass
class ComputeTable:
    """A simple compute table implementation.

    This class is used to cache the results of operations on DDs. It is really
    just a dictionary that maps tuples of (operand1, operand2, operation) to
    the result of the operation. It uses no collision resolution, and just
    overwrites existing entries upon insertion. This is not a very efficient
    implementation, but it is sufficient for our purposes.

    Attributes:
        table: The dictionary that maps tuples of (operand1, operand2, operation)
        to the result of the operation.
    """

    table: dict[tuple[DD, DD, DDOperation], DD]

    def __init__(self) -> None:
        """Initializes an empty compute table."""
        self.table = {}

    def lookup(self, operand1: DD, operand2: DD, operation: DDOperation) -> DD | None:
        """Looks up a node in the compute table.

        Args:
            operand1: The first operand.
            operand2: The second operand.
            operation: The operation to apply.

        Returns:
            The result of the operation if it is in the table, or None if it is not.
        """
        key = (operand1, operand2, operation)
        if key in self.table:
            return self.table[key]
        return None

    def insert(self, operand1: DD, operand2: DD, operation: DDOperation, result: DD) -> None:
        """Inserts a node into the compute table.

        Args:
            operand1: The first operand.
            operand2: The second operand.
            operation: The operation to apply.
            result: The result of the operation.
        """
        key = (operand1, operand2, operation)
        self.table[key] = result

    def clear(self) -> None:
        """Clears the compute table."""
        self.table.clear()


################################################################################
# Global constants and utility methods                                         #
################################################################################

# There is a unique terminal node
TERM = DDNode(-1, [])

# The following two DDs are (unique) the zero and one terminal nodes
ZERO_TERM = DD(TERM, np.complex128(0))
ONE_TERM = DD(TERM, np.complex128(1))

# Unique table
UT = UniqueTable()

# Compute table
CT = ComputeTable()


def __vector_normalization(node: DDNode) -> DD:
    """Normalizes a vector DD node.

    Args:
        node: The node to normalize.

    Returns:
        A normalized DD.

    Note:
        Normalization is essential for ensuring that DDs are canonical. It
        ensures that two functionally equivalent DDs are actually identical.
        This is important for the unique table to work correctly.
        For vectors, the most commonly used normalization is to ensure that the
        squared magnitudes of the outgoing edges sum to 1.
    """
    succ0 = node.successors[0]
    succ1 = node.successors[1]
    if succ0.is_zero_terminal():
        if succ1.is_zero_terminal():
            return ZERO_TERM
        weight = succ1.weight
        succ1.weight = 1
        return DD(node, weight)

    if succ1.is_zero_terminal():
        weight = succ0.weight
        succ0.weight = 1
        return DD(node, weight)

    mag2_0 = np.abs(succ0.weight) ** 2
    mag2_1 = np.abs(succ1.weight) ** 2
    norm2 = mag2_0 + mag2_1
    mag2_max = max(mag2_0, mag2_1)
    arg_max = 0 if mag2_0 >= mag2_1 else 1
    arg_min = 1 - arg_max
    norm = np.sqrt(norm2)
    mag_max = np.sqrt(mag2_max)
    common_factor = norm / mag_max

    top_weight = node.successors[arg_max].weight * common_factor
    if np.isclose(top_weight, 0):
        return ZERO_TERM

    new_max_weight = mag_max / norm
    new_min_weight = node.successors[arg_min].weight / top_weight
    if np.isclose(new_max_weight, 0):
        node.successors[arg_max] = ZERO_TERM
    else:
        node.successors[arg_max].weight = new_max_weight

    if np.isclose(new_min_weight, 0):
        node.successors[arg_min] = ZERO_TERM
    else:
        node.successors[arg_min].weight = new_min_weight

    return DD(node, top_weight)


def __matrix_normalization(node: DDNode) -> DD:
    """Normalizes a matrix DD node.

    Args:
        node: The node to normalize.

    Returns:
        A normalized DD.

    Note:
        Normalization is essential for ensuring that DDs are canonical. It
        ensures that two functionally equivalent DDs are actually identical.
        This is important for the unique table to work correctly.
        For matrices, the most commonly used normalization is to divide each
        entry by the maximum magnitude of all entries. If there are multiple
        entries with the same maximum magnitude, the first one is chosen.
    """
    if all(succ.is_zero_terminal() for succ in node.successors):
        return ZERO_TERM

    weights = [succ.weight for succ in node.successors]
    arg_max = np.argmax(np.abs(weights))
    max_weight = weights[arg_max]
    new_weights = [weight / max_weight for weight in weights]
    for i in range(len(weights)):
        node.successors[i].weight = new_weights[i]

    return DD(node, max_weight)


def make_dd(v: int, successors: list[DD]) -> DD:
    """The main function for creating new DDs and DD Nodes.

    Args:
        v: The index of the qubit associated with this node.
        successors: The list of successors..

    Returns:
        A normalized DD with the newly created node (or the node from the unique
        table if it already existed).

    Raises:
        AssertionError: If the index of the qubit is negative, or if the number
        of successors is not 2 or 4.

    Note:
        This function is the main entry point for creating new DDs. It ensures
        that the DD is normalized, and that the node is unique.
        The length of the successors list determines whether the node is a
        vector or a matrix node. For vectors, the list must contain exactly two
        elements, and for matrices, the list must contain exactly four elements.
        For example, creating a vector DD for the one-qubit |0> state can be
        done as follows:
            zero_state = make_dd(0, [DD(TERM, 1), DD(TERM, 0)])
        The same can be achieved by using the predefined ONE_TERM and ZERO_TERM
        constants:
            zero_state = make_dd(0, [ONE_TERM, ZERO_TERM])
    """
    assert v >= 0, """
    v must be non-negative.
    Terminals should be constructed using the unique terminal as `DD(TERM, weight)`.
    """
    assert len(successors) in {2, 4}, """
    DD must have either 2 or 4 successors to be a vector or matrix, respectively.
    """
    node = DDNode(v, successors)
    dd = __vector_normalization(node) if len(successors) == 2 else __matrix_normalization(node)

    node = UT.lookup(dd.node)
    return DD(node, dd.weight)
