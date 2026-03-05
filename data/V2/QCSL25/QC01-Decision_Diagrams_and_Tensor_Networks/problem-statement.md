# Decision Diagrams Simulation

Throughout this exercise, we will be implementing a statevector simulator for
quantum circuits. This simulator will be based on decision diagrams, and will
implement the basic functionality of a quantum computer. This will be used
to simulate the creation of GHZ states, which are generalizations of the Bell
states.

Note:

- The qubit ordering is assumed to be $$q_{N-1} \dots q_1 q_0$$, i.e., the least
significant qubit is the rightmost one. Any computational basis state $$|i\rangle$$
is represented by the bitstring $$i$$ in big-endian form. For example, the
state |100> would be represented by the bitstring '$$100$$', i.e., the value $$4$$.
In that case, $$q_2 = 1$$, $$q_1 = 0$$, and $$q_0 = 0$$.

- The basic functionality for working with decision diagrams is already
implemented in `dd.py`. You should not need to modify that file. However,
you should read it carefully to understand the basic functionality of
decision diagrams.
Throughout this exercise, you should use the functions defined in `dd.py`
to create and manipulate decision diagrams. You should not directly
manipulate the `DD` class or the `DDNode` class.

You have the following tasks:

[task][1. Create zero state](test_dd_zero_state)

Implement the function '`dd_create_zero_state`' that returns a DD corresponding to the zero state $$|0\dots0\rangle$$ of an $$N$$-qubit system.

[task][2. Create single qubit gate](test_single_qubit_gate)

Implement the function '`create_single_qubit_gate`' 
to create a DD representation of a single-qubit gate on the specified target qubit with the specified gate matrix in an $$N$$-qubit system.

[task][3. Create controlled single qubit gate](test_controlled_gate)

Implement the function '`create_controlled_single_qubit_gate`' to create a DD representation of the controlled version of a single-qubit gate on the specified control and target qubits with the specified gate matrix in an $$N$$-qubit system.

[task][4. Add two DDs](test_addition)

Implement the function '`add`' to add two given DDs. This is required as part of multiplying DDs.

[task][5. Multiply two DDs](test_multiplication)

Implement the function '`multiply`' to multiply two given DDs.

[task][6. Get amplitude](test_dd_get_amplitude)

Implement the function '`dd_get_amplitude`' to return the amplitude corresponding to the given bitstring.

[task][7. Measure](test_dd_measure_all)

Implement the function '`dd_measure_all`' to measure all qubits in the computational basis repeatedly and to return the number of times each result was measured.

[task][8. Simulate the GHZ state](test_dd_simulate_ghz_state)

Implement the function '`dd_simulate_ghz_state`' to simulate a circuit to create an $$N$$-qubit $$GHZ$$ state.

# Tensor Networks

Throughout this exercise, we will be implementing a tensor network simulator for
quantum circuits. This will be used to simulate the creation of $$GHZ$$ states,
which are generalizations of the Bell states.

*Note*:
    
- The qubit ordering is assumed to be $$q_{N-1} \dots q_1 q_0$$, i.e., the least
significant qubit is the rightmost one. Any computational basis state $$|i\rangle$$
is represented by the bitstring $$i$$ in big-endian form. For example, the
state |100> would be represented by the bitstring '$$100$$', i.e., the value $$4$$.
In that case, $$q_2 = 1$$, $$q_1 = 0$$, and $$q_0 = 0$$.

You have the following tasks:

[task][1. Create zero state](test_zero_state)

Implement the function `create_zero_state` to return an $$MPS$$ corresponding to the zero state $$|0\dots0\rangle$$ of an $$n$$-qubit system. Note that the final shape of a site should be (1,2,1), i.e. trivial bond dimension and the physical dimension in the middle.

[task][2. Create nearest-neighbor two qubit gate](test_nearest_neighbor_two_qubit_gate)

Implement the function `create_nearest_neighbor_two_qubit_gate` that creates a two-qubit gate `W` from a given gate matrix. Use `np.reshape` here.

[task][3. Apply single qubit gate](test_apply_single_qubit_gate)

Implement the function `apply_single_qubit_gate` to apply a single-qubit gate to an $$MPS$$. It should act directly on the $$MPS$$ list. Use `np.einsum` as explained in the lecture.

[task][4. Apply two qubit gate](test_apply_two_qubit_gate)

Implement the function `apply_two_qubit_gate` to apply a two-qubit gate to an $$MPS$$. It should act directly on the $$MPS$$ list. Use `np.einsum` as explained in the lecture.

[task][5. Get amplitude](test_get_amplitude)

Implement the function `get_amplitude` to return the amplitude corresponding to a given bitstring.

[task][6. Measure all](test_measure_all)

Implement the function `measure_all` to measure all qubits in the computational basis repeatedly and
    return the number of times each result was measured.

[task][7. Simulate GHZ](test_simulate_ghz_state)

Implement the function `simulate_ghz_state` to simulate a circuit to create an $$n$$-qubit $$GHZ$$ state.