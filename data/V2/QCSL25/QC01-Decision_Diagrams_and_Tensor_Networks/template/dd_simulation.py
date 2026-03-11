# ruff: noqa: F401
"""A basic implementation of a statevector simulator based on decision diagrams.

Throughout this exercise, we will be implementing a statevector simulator for
quantum circuits. This simulator will be based on decision diagrams, and will
implement the basic functionality of a quantum computer. This will be used
to simulate the creation of GHZ states, which are generalizations of the Bell
states.

The simulator will be based on the following functions:
    dd_create_zero_state(num_qubits)
    create_single_qubit_gate(num_qubits, target, gate_matrix)
    create_controlled_single_qubit_gate(num_qubits, control, target, gate_matrix)
    add(dd1, dd2)
    apply_gate(state, gate)
    dd_get_amplitude(state, bitstring)
    dd_measure_all(state, shots)
    dd_simulate_ghz_state(num_qubits, shots)

Note:
    The qubit ordering is assumed to be q_{N-1} ... q_1 q_0, i.e., the least
    significant qubit is the rightmost one. Any computational basis state |i>
    is represented by the bitstring i in big-endian form. For example, the
    state |100> would be represented by the bitstring '100', i.e., the value 4.
    In that case, q_2 = 1, q_1 = 0, and q_0 = 0.

Important:
    The basic functionality for working with decision diagrams is already
    implemented in `dd.py`. You should not need to modify that file. However,
    you should read it carefully to understand the basic functionality of
    decision diagrams.
    Throughout this exercise, you should use the functions defined in `dd.py`
    to create and manipulate decision diagrams. You should not directly
    manipulate the `DD` class or the `DDNode` class.

    Most of the functions in this file are supplemented with hints and comments
    that explain how to implement them. You should read these carefully.
    Note that in many cases, there might be multiple ways to implement a
    function. The hints and comments are meant to guide you towards a
    particular implementation, but you are free to implement the function
    differently if you want to (as long as the function behaves as specified).
"""

from __future__ import annotations

from collections import defaultdict
from itertools import starmap
from typing import TYPE_CHECKING

import numpy as np
from .dd import CT, DD, ONE_TERM, TERM, ZERO_TERM, DDOperation, make_dd

if TYPE_CHECKING:
    from numpy.typing import NDArray


def dd_create_zero_state(num_qubits: int) -> DD:
    """
    This function returns a DD corresponding to the zero state |0...0> of
    an n-qubit system.

    Args:
        num_qubits: The number of qubits in the system.

    Returns:
        A DDNode corresponding to the n-qubit zero state.
    """
    assert num_qubits > 0

    # create the `DD` for the zero state (=[1 0]^T) on qubit 0 (using `make_dd`)
    # and the predefined terminal DDs `ZERO_TERM` and `ONE_TERM`.
    # TODO

    # Augment the `DD` for the zero state on the first qubit to a `DD` for the
    # zero state on n qubits by repeatedly creating new nodes (and `DD`s) that
    # build on the previous `DD`s.
    # Remember: |0...0> = |0...0> x |0> = ... = |0> x ... x |0>
    # TODO

    # return the resulting `DD`
    pass


def create_single_qubit_gate(num_qubits: int, target: int, gate_matrix: NDArray[np.complex128]) -> DD:
    """
    This function creates a DD representation of a single-qubit gate on the
    specified target qubit with the specified gate matrix in an N-qubit system.

    Args:
        num_qubits: The number of qubits in the system.
        target: The target qubit for the gate.
        gate_matrix: The 2x2 matrix corresponding to the gate being applied.

    Returns:
        A DDNode corresponding to the gate.

    Note:
        To apply a single-qubit gate to a multi-qubit system, we take
        the tensor product of the single-qubit gate matrix with the identity
        matrix on the non-target qubits. For example, if we want to apply the
        gate U to qubit q_3 in a 5-qubit system, we compute
        I x U x I x I x I, where x denotes the tensor product.
        For decision diagrams, the tensor product is implemented by stacking
        the DDs for the individual qubits on top of each other.
        In the context of computing A x B (with A and B being DDs), stacking
        here means to replace the terminal nodes of A with the root node of B
        (and potentially adjusting the indices).
    """
    # the gate matrix should be 2x2
    assert gate_matrix.ndim == 2
    assert gate_matrix.shape == (2, 2)
    # the number of qubits should be positive
    assert num_qubits > 0
    # the target qubit should be in the range of the number of qubits
    assert 0 <= target < num_qubits

    # if the target is at qubit zero, directly create a matrix node from the
    # gate matrix.
    if target == 0:
        # create a `DD` for [U00 U01 U10 U11]
        # TODO

        # Augment the `DD` with DDs for the identity matrices on the remaining
        # qubits. Schematically dd(v+1) = [dd(v) 0 0 dd(v)]
        # TODO

        # return the resulting `DD`
        # TODO
        pass

    # if the target is not at qubit zero, create the DD bottom-up by creating
    # levels of identity matrices for every qubit below the target qubit.
    # TODO

    # create the individual DDs for [U00 U01 U10 U11] on top of the identity matrices
    # If any entry is close to zero, we can just use the zero terminal node `ZERO_TERM`.
    # Otherwise, we need to create a new `DD` for the entry with the corresponding
    # value as weight and the previously created `DD` as node.
    # Note: YOu can use `np.isclose` to check if a value is close to zero.
    # TODO

    # combine the individual DDs into a single DD for the gate
    # TODO

    # Augment the `DD` with DDs for the identity matrices on the remaining
    # qubits. Schematically dd(v+1) = [dd(v) 0 0 dd(v)]
    # TODO

    # return the resulting `DD`
    pass


def create_controlled_single_qubit_gate(
    num_qubits: int, control: int, target: int, gate_matrix: NDArray[np.complex128]
) -> DD:
    """
    This function creates a DD representation of the controlled version of
    a single-qubit gate on the specified control and target qubits with the
    specified gate matrix in an N-qubit system.

    Args:
        num_qubits: The number of qubits in the system.
        control: The control qubit for the gate.
        target: The target qubit for the gate.
        gate_matrix: The 2x2 matrix corresponding to the gate being applied.

    Returns:
        A DDNode corresponding to the gate.

    Note:
        This is a bit trickier than the previous functions. The idea is that we
        want to apply the gate_matrix to the target qubit if the control qubit
        is in the state |1>. There are multiple ways to accomplish this.

        For simplicity, we assume that the control qubit is above the target.
        This makes constructing the DD a little easier. The general structure
        then resembles the following:
        I^(n-c) x [ I^(c) | 0  ]
                  [ 0     | U' ]
        where I is the identity matrix and `x` denotes the tensor product.
        More precisely, the DD is constructed as follows:
        1. Create a DD for the (c)-qubit identity matrix I^(c) This can be
           done by calling `create_single_qubit_gate` with the identity matrix.
        2. Create a DD for the (c)-qubit single-qubit gate U applied to the
           target qubit. This can be done by calling `create_single_qubit_gate`.
        3. Create a DD for the control level by appropriately combining the
           DDs from steps 1 and 2.
        4. Add the remaining identity matrices I^(n-c) to the DD from step 3.
    """
    # the gate matrix should be 2x2
    assert gate_matrix.ndim == 2
    assert gate_matrix.shape == (2, 2)
    # the number of qubits should be positive
    assert num_qubits > 0
    # the control qubit should be in the range of the number of qubits
    assert 0 <= control < num_qubits
    # the target qubit should be in the range of the number of qubits
    assert 0 <= target < num_qubits
    # the control and target qubits should be different
    assert control > target

    # Step 1:
    # TODO

    # Step 2:
    # TODO

    # Step 3:
    # TODO

    # Step 4:
    # TODO

    # return the resulting `DD`
    # TODO
    pass


def add(dd1: DD, dd2: DD) -> DD:
    """
    This function adds two DDs. This is required as part of multiplying DDs.

    Args:
        dd1: The first DD to add.
        dd2: The second DD to add.

    Returns:
        A DDNode corresponding to the sum.

    Note:
        This is a little more complicated then for statevector simulators.
        The idea is to realize addition directly on the DDs.
        To this end, the addition is recursively carried out according to
        the following decomposition (for vectors):

        [psi0]   [phi0]   [psi0 + phi0]
        [----] + [----] = [-----------]
        [psi1]   [phi1]   [psi1 + phi1]

        Implement this using the unique table and compute table data structures
        defined above.
    """
    # Step 1: Handle terminal cases
    # Step 1.1: If one of the DDs is a zero terminal, return the other DD
    # TODO

    # At this point we can assert that both DDs are equally high.
    assert dd1.num_qubits() == dd2.num_qubits()

    # Step 1.2: If both are non-zero terminals, return a new terminal with the sum of the weights
    # TODO

    # Step 1.3: If both DDs point to the same node, return a new DD with the sum of the weights
    # If the resulting weight is zero, return the zero terminal
    # TODO

    # Step 2: Check if the result is already in the compute table and return it
    # TODO

    # Step 3: Compute the result by recursively adding the successors
    # Step 3.1: Multiply the weights of all successors with the weight of the current node
    # TODO

    # Step 3.2: Add the respective pairs of successors
    # TODO

    # Step 4: Create a new node with the computed successors.
    # If all the successors are zero terminals, the result is a zero terminal.
    # TODO

    # Step 5: Insert the result into the compute table and return it
    # TODO

    # return the resulting `DD`
    # TODO
    pass


def multiply(gate: DD, state: DD) -> DD:
    """
    This function computes the matrix-vector product of a gate and a state in DD form.

    Args:
        gate: The first operand
        state: The second operand

    Returns:
        A DD corresponding to the product.

    Note:
        This is a little more complicated then for statevector simulators.
        The idea is to realize matrix-vector multiplication with the DDs.
        To this end, the multiplication is recursively carried out according to
        the following decomposition (for vectors):

        [psi0]   [ U00 U01 ]   [psi0]   [ U00 psi0 + U01 psi1 ]
        [----] x [---------] = [----] = [---------------------]
        [psi1]   [ U10 U11 ]   [psi1]   [ U10 psi0 + U11 psi1 ]

        Implement this using the unique table and compute table data structures
        defined above.
    """
    # Step 1: Handle terminal cases
    # Step 1.1: If any of the operands is a zero terminal, return the zero terminal
    # TODO

    # At this point we can assert that both DDs are equally high.
    assert gate.num_qubits() == state.num_qubits()

    # Step 1.2: If the operands are terminals, return a new terminal with the product of the weights
    # TODO

    # Step 2: Check if the result is already in the compute table and return it
    # TODO

    # Step 3: Compute the four sub-products
    # TODO

    # Step 4: Add the respective pairs of sub-products
    # TODO

    # Step 5: Create a new node with the computed successors.
    # If all the successors are zero terminals, the result is a zero terminal.
    # Make sure to account for the weight of the gate and the state.
    # TODO

    # Step 5: Insert the result into the compute table and return it
    # TODO

    # return the resulting `DD`
    # TODO
    pass


def apply_gate(state: DD, gate: DD) -> DD:
    """
    This function applies a given gate to a given state.

    Args:
        state: The state to which the gate is applied.
        gate: The gate to be applied.

    Returns:
        The new state after applying the gate.
    """
    # both should act on the same number of qubits
    assert state.num_qubits() == gate.num_qubits()
    # the state DD should be a vector
    assert state.is_vector()
    # the gate DD should be a matrix
    assert gate.is_matrix()
    return multiply(gate, state)


def dd_get_amplitude(state: DD, bitstring: str) -> np.complex128:
    """
    This function returns the amplitude corresponding to a given bitstring.

    Args:
        state: The state from which the amplitude is extracted.
        bitstring: The bitstring for which the amplitude is extracted.

    Returns:
        The amplitude corresponding to the given bitstring.

    Note:
        In order to extract the amplitude for a given bitstring, we need to
        recursively traverse the DD. The amplitude is the product of all edge
        weights along the path corresponding to the bitstring.
        Beware of the qubit and bitstring ordering! The bitstring is in
        big-endian form, i.e., the most significant bit is on the left.
        Specifically, `bitstring[i]` corresponds to qubit `num_qubits - 1 - i`.
    """
    #  the state DD should be a vector
    assert state.is_vector()
    num_qubits = state.num_qubits()
    # the bitstring should have the same length as the number of qubits
    assert len(bitstring) == num_qubits

    # Recursively traverse the DD and compute the amplitude by multiplying the
    # edge weights along the path corresponding to the bitstring.
    # TODO

    # return the resulting amplitude
    # TODO
    pass


def dd_measure_all(state: DD, shots: int) -> dict[str, int]:
    """
    This function measures all qubits in the computational basis repeatedly and
    returns the number of times each result was measured.

    Args:
        state: The state to be measured.
        shots: The number of times to sample the state.

    Returns:
        A dictionary mapping each result (bitstring) to the number of times it
        was measured. For example, {'00': 5, '11': 19} would mean that the
        bitstring '00' was measured 5 times and the bitstring '11' was measured
        19 times.

    Note:
        Due to the way vector DDs are normalized, the probability of measuring
        '0' or '1' at a particular level in the DD is the squared magnitude of
        the corresponding edge weight. Thus, as single sample/shot can be drawn
        by traversing the DD and sampling a bit at each level according to the
        probability distribution given by the squared magnitudes of the edge
        weights.
    """
    # the state DD should be a vector
    assert state.is_vector()
    # the number of shots should be positive
    assert shots > 0

    counts = defaultdict(int)
    gen = np.random.Generator(np.random.PCG64(seed=12345))

    for _ in range(shots):
        # TODO
        pass

    return dict(counts)


def dd_simulate_ghz_state(num_qubits: int, shots: int) -> dict[str, int]:
    """
    This function simulates a circuit to create an n-qubit GHZ state.

    Args:
        num_qubits: The number of qubits in the system.
        shots: The number of times to sample the state.

    Returns:
        A dictionary mapping each result (bitstring) to the number of times it
        was measured.

    Note:
        The GHZ state is a generalization of the Bell state to multiple qubits.
        It is defined as 1/sqrt(2) * (|0...0> + |1...1>).

        To perform the simulation, you should do the following:

        1. Initialize the structures needed, i.e., create the starting state
        |0...0> and the local (one- and two-qubit) H and CNOT matrices.

        2. Create the gates at their corresponding target locations.

        3. Apply gates to the state to simulate a circuit.

        4. Measure the states with some input number of shots.
    """
    # the number of qubits should be positive
    assert num_qubits > 0
    # the number of shots should be positive
    assert shots > 0
    # 1. Initialize the structures needed
    # TODO

    # 2. Create the gates at their corresponding target locations
    # TODO

    # 3. Apply gates to the state
    # TODO

    # 4. Measure state
    # TODO

    # return the resulting counts
    # TODO
    pass
