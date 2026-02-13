# Magic State Distillation

In this exercise, you will implement and simulate the distillation of a $\ket{Y} = S\ket{+}$ state using stim. While $\ket{Y}$ states are not magic states, i.e., non-Clifford, the protocol works almost the same, and the fact that $\ket{Y}$ is a stabilizer state makes it easy to simulate large distillation circuits using stim.

After completing this exercise, you should be able to:

- Understand and construct state preparation circuits for CSS codes.
- Implement gate teleportation protocols for magic state injection.
- Assemble a full 15-to-1 magic state distillation protocol.
- Simulate noisy state distillation using stim, and evaluate fidelity and acceptance of the output state."

## Overview 

Distillation is usually performed on logical qubits. Since we are only interested in the distillation circuit, we will perform the distillation directly on physical qubits and restrict our gate set to those we can implement fault-tolerantly on the surface code. We assume the only error-prone part of the protocol is the preparation of $\ket{Y}$ states, which are subject to depolarizing noise of strength $p$.

The distillation procedure we will perform is as follows:

- Prepare 15 ancilla qubits in the logical $\ket{0}_L$ state of the $[[15,1,3]]$ "tetrahedral" code.
- Initialize a qubit $q$ in $\ket{+}$ and perform gates $CX_q^{\mathrm{anc}_i}$ for all qubits $\mathrm{anc}_i$ in the tetrahedral code.
- The system is now in Bell state between the physical qubit $q$ and the logical qubit $\ket{0}\ket{0}_L + \ket{1}\ket{1}_L$.
- The tetrahedral code has a tranversal $S$ gate, so perform $S^{\otimes 15}$ on the 15 qubits of the tetrahedral code via gate teleportation.
- The system is now in the state $\ket{0}\ket{0}_L + e^{i\pi/2}\ket{1}\ket{1}_L = \ket{Y}\ket{+}_L - \ket{Y}\ket{-}_L$.
- Measure out the logical qubit in the $X$ basis. 
- If any error is detected in this measurement, discard the state and restart the distillation procedure.
- If no error is detected, $q$ should now be either in $\ket{Y}$ or $-\ket{Y}$.
- Apply a $Z$ correction to $q$ depending on the outcome of the logical $X$ measurement.

As a circuit, the distillation procedure looks as follows:

![distillation.png](/api/core/files/markdown/Markdown_2025-07-23T23-17-00-204_48a375c8.png)

## State Preparation

The first stage of the distillation protocol requires the preparation of a logical zero state of a CSS code.

The logical zero state of a stabilizer code is a stabilizer state defined by the stabilizers and the logical $Z$ operator of the code. 
A state preparation circuit for this code is a circuit that, after qubit initialization, transforms the stabilizer group at the beginning of the circuit into the stabilizer group of the stabilizer state.
In other words, a state preparation circuit takes the tableau $[0|I]$ and maps it to the tableau representation of the stabilizers of the state (up to arbitrary row operations).

For CSS codes, the situation is simpler. A CSS code is a stabilizer code with a generating set that can be partitioned into "X"-type and "Z"-type stabilizers. These stabilizers are tensor products of only $X$ and $I$ or $Z$ and $I$, respectively. The logical operators of a CSS code are also all of one type (Z-operators are Z-type and X-operators are X-type). The Steane code is one example of a CSS code. The tableau representation of a CSS code is therefore: 

$$\begin{bmatrix}H_X & 0 \\ 0 & H_Z\end{bmatrix}.$$

The matrices $H_X$ and $H_Z$ are called the check matrices of the CSS code. Since all stabilizers of a code must commute, we get the "CSS condition" $H_X H_Z^T=0$. Furthermore, for the logical Z operator $L_Z$, we also have $H_X L_Z = 0$. Therefore, the structure of CSS codes allows for a straightforward state preparation circuit synthesis methodology. 

- Start with the check matrix of the code $H_X$. 
- Apply Gaussian elimination to the columns of $H_X$ to obtain a matrix that has exactly $\mathrm{rk}(H_X)$ non-zero columns. Every column addition $c_j \mathrel{+}= c_i$ corresponds to a CNOT gate with control on qubit $i$ and target on qubit $j$.
- We now have a sequence of CNOT gates that reduces $H_X$.
- Initialize qubits corresponding to non-zero columns in the reduced matrix in $\ket{+}$.
- Initialize qubits corresponding to zero columns in the reduced matrix in $\ket{0}$.
- Apply the inverse of the CNOT sequence obtained through Gaussian elimination.

This method works because CNOTs map X-stabilizers to X-stabilizers and Z-stabilizers to Z-stabilizers. So commuting X- and Z-stabilizers before the CNOT circuit will be mapped to commuting X- and Z-stabilizers after the circuit. The orthogonal complement of a vector space is uniquely defined. So if the CNOT circuit maps the X-stabilizers at the beginning of the circuit (the single-qubit X operators on the $\ket{+}$ states) to a basis of the rowspace of $H_X$ then we also know that the Z-stabilizers at the beginning of the circuit (the single-qubit Z operators on the $\ket{0}$ states) are mapped to a basis of the rowspace of $$\begin{bmatrix}H_Z \\ L_Z\end{bmatrix}.$$

[task][a. Logical Zero state preparation](test_state_preparation[steane_code_hx],test_state_preparation[tetrahedral_code_hx])
Implement the function 

```python
construct_zero_state_prep_circuit(Hx: npt.NDArray[np.int8], offset: int=0) -> stim.Circuit
```
    
which constructs a state preparation Stim circuit from the X-check matrix of a CSS code on qubits `offset` until `offset+n` where `n` is the number of qubits of the code. You are only allowed to use the instructions `RX`, `R`, and `CX`. 


## Gate Teleportation

When distilling states, we (usually) cannot perform a gate directly on the qubits of the tetrahedral code (otherwise, we wouldn't need to distill them). Rather, one needs to inject states via gate teleportation. For $\ket{Y}$ states, the teleportation protocol is described by the following ZX-diagram:

![s_injection.png](/api/core/files/markdown/Markdown_2025-07-21T15-36-23-326_fcda11df.png)

The measurement of the ancilla state is not deterministic, so a correction needs to be applied to the data in case the measurement result is non-trivial. Before implementing the following functions, figure out what the correction should be and how it affects measurement results of the data qubit in the $X$ basis.

For this part you are only allowed to use the instructions `S`, `DEPOLARIZE1`, `RX`, `H`, `MR`, `MRX`, `R`, and `CX`.

[task][a. Prepare a resource state](test_make_y_state)
Implement the function

```python
make_y_state(circ: stim.Circuit, q: int, p: float) -> None
```

which prepares qubit `q` in $\ket{Y}$ subject to single-qubit depolarizing noise of strength `p`.


[task][b. Construct injection circuit](test_injection)
Implement the function 

```python
inject(circ: stim.Circuit, data_qubit: int, injection_qubit) -> None
```
 
which constructs the injection circuit in which the `injection_qubit` is measured. The function should return the measurement index in the Stim circuit (this will be needed for correction later).

[task][c. Construct full teleportation circuit with corrections](test_teleport_s)
Implement the function

```python
teleport_s(circ: stim.Circuit, data_qubit: int, injection_qubit: int, p = 0.0) -> int
```
 
which combines the $\ket{Y}$ state preparation and injection. The function should return the index of the measurement in the Stim circuit (this is needed for the correction later).

Implement the function

```python
correct_teleportation(teleportation_measurements: npt.NDArray[np.int8], x_measurements: npt.NDArray[np.int8]) -> npt.NDArray[np.int8]
```
    
which takes an array of measurement results from gate teleportations and corresponding $X$ basis measurements and returns an array of corrections. $0$ corresponds to not flipping the $X$ measurement and $1$ corresponds to flipping the $X$ measurement.

## Distillation Circuit

[task][a. Construct the distillation circuit](test_build_msd_circ)
Implement the function 

```python
build_msd_circ(circ: stim.Circuit, distilled_state: int, y_states:list[int]) -> tuple[list[int], list[int]] 
```
    
which takes a stim circuit and constructs the distillation circuit using the qubits indexed by `y_states` as $\ket{Y}$ resource states and distills a $\ket{Y}$ state onto qubit `distilled_state`. The function should return two lists for measurement indices, the first corresponding to the measurements performed for the $\ket{Y}$ state injections, and the second corresponding to the destructive measurements of the 15 qubits of the tetrahedral code state (make sure that the order of measurements conforms to the ordering of the qubits).

You are only allowed to use the instructions `RX`, `R`, `CX`, `MR`, and `MRX`. Do not prepare a $\ket{Y}$ state on the `y_states` qubits. The states are assumed to be already prepared in `circ`.

## Detecting Errors during Distillation

[task][a. Implement error detection](test_detect_error)
We want to detect errors that occurred during injection of the impure $\ket{Y}$ states. We can use the result of the destructive $X$ basis measurements to achieve this. Implement the function

```python
detect_errors(measurements: npt.NDArray[np.int8], checks: npt.NDArray[np.int8]) -> npt.NDArray[np.int8]
```
    
which takes a two-dimensional array of measurements (every row corresponds to a measurement) and a check matrix and returns a one-dimensional binary array `error` with `error[i]=1` if and only if **no error** is detected in row `measurements[i]`.  

## Simulating One Round of MSD

[task][a. Simulate the Distillation Protocol](test_msd_noiseless,test_simulate_msd_one_round)
Finally, we want to put everything together and simulate the distillation protocol. We want to estimate the error and acceptance rates of the distillation protocol. Let $\mathrm{s}$ be the number of simulated shots, $\mathrm{gs}$ be the number of "good" shots, i.e. shots where no error was detected, and $\mathrm{f}$ be the number of shots where the state $-\ket{Y}$ was distilled instead of $\ket{Y}$. 
Then the error rate is estimated as 

$$\mathrm{err} = \mathrm{f}/\mathrm{gs},$$

and the acceptance rate is estimated as 

$$\mathrm{acc} = \mathrm{gs}/\mathrm{s}.$$

Implement the function

```python
simulate_msd_one_round(n_shots:int, p: float) -> tuple[float, float]
```
 
which simulates one round of distillation. The function should run `n_shots` simulation rounds and use an injection error of `p`. The function should return the estimated error rate and the acceptance rate of the simulation. 

Use the methods you have implemented in the previous tasks to achieve this. Consider the following:

- To estimate the error, you need to detect whether the distilled state is in the $\ket{Y}$ or $-\ket{Y}$ state. What circuit do you need to perform to measure this? You are allowed to use any Stim instruction for this part.

- The $X$ basis measurement is not deterministic. Even in the error-free case, the logical state is randomly measured to be in $\ket{+}$ or $\ket{-}$. What correction must you apply to the $\ket{Y}$ measurements of the distilled state?

You can use the function `plot_msd` to plot your distillation. If you implemented the distillation correctly, the error rate should scale as $O(p^3)$. 

## Bonus Task: Simulate Two Rounds of Distillation

After one round of distillation, we obtain a $\ket{Y}$ state with an error rate of $\ket{O(p^3)}$. Depending on the physical error rate $p$ we started with, the error rate of the distilled state might not be low enough for a given quantum algorithm. To suppress the error rate even lower one can distill $15$ states in parallel and use them as the resource states of the next round of distillation.

[task][a. Simulate two Rounds of Distillation](test_msd_two_rounds_noiseless,test_simulate_msd_two_rounds)

Implement the function

```python
simulate_msd_two_rounds(n_shots:int, p: float, batch_size:int) -> tuple[float, float]
```
 
which simulates two round of distillation. The function should run `n_shots` simulation rounds and use an injection error of `p`. The function should return the estimated error rate and the acceptance rate of the simulation. 

We do not want to deal with classical control flow for the simulation. Instead, you should implement one big circuit that represents two rounds of distillation. Use the `test_build_msd_circ` function repeatedly to construct this circuit.

Think about how to handle the measurement results of the individual distillation circuits. Remember that one round of distillation non-deterministically distills a $\ket{Y}$ or $-\ket{Y}$ state depending on the logical $X$ measurement.

You can use the function `plot_msd_two_rounds` to plot your distillation. If you implemented the distillation correctly, the error rate should scale as $O(p^9)$. 

Due to the low error rate of the protocol, a lot of samples are needed to properly estimate the error rate of two rounds of measurement. Depending on your machine, running large simulation ($\sim 10^7$ shots) might use up all of the available RAM. Therefore, implement `simulate_msd_two_rounds` such that the simulation is done in batches. Choose a reasonable batch size. 