<span class="red">**Note: Use Light Mode when viewing these exercises as the images have dark fonts in them.**</span>

# Grover's Algorithm

Today we will work through examples around Grover's algorithm, one of the most famous quantum algorithms. 

Let us recap the basics of Grover's algorithm in a hands-on way with Qiskit. 

This algorithm can speed up an unstructured search problem <span style="color:blue">**quadratically**</span> (a classical computation requires on the order of $$N$$ steps to search $$N$$ entries problem, while a quantum computer requires just $$\sqrt{N}$$), but its uses extend beyond that; it often serves as subroutine to obtain quadratic run time improvements for a variety of other algorithms. This is called the amplitude amplification trick.

In the following we will discuss the description of the search problem, building the oracle - the circuit representation of our search problem, and implement the complete Grover algorithm in Qiskit.

## Unstructured search

Suppose we are given a large list of $$N$$ items. Among these items there is one item with a unique property that we wish to locate; we will call this one the winner, $$w$$. Think of each item in the list as a box of a particular item. Say all items in the list have grey colored items except the winning item.

The situation looks like this:

![fig1.png](/api/core/files/markdown/Markdown_2023-11-08T17-56-39-439_95025161.png)

To find the winning item -- the marked item -- using classical computation, one would have to check on average $$N/2$$ of these boxes, and in the worst case, all $$N$$ of them (which is exponential in the input size $$n$$). On a quantum computer we can find the marked item in roughly $$\sqrt{N}$$ steps with Grover's algorithm. 
A quadratic speedup is indeed a substantial time-saver for finding marked items in long lists. Additionally, the algorithm does not use the list's internal structure, which makes it very general; this is why it immediately provides a quadratic quantum speed-up for many classical problems.

## Creating an oracle that marks the winning item

How do we represent the database/list in order to use our standard problem formulation? A common way is to view it as (the truth table of a) function $$f$$ that returns $$f(x)=0$$ for all unmarked items $$x$$, and $$f(w)=1$$ for the winner. As for the previous algorithms, in order to use a quantum computer (circuit) for this problem, we encode the function into a unitary matrix called an **oracle**. 

First, we choose a binary encoding of the items $$x,w \in \{0,1\}^n$$ so that $$N=2^n$$. We then define a sign-implementation circuit for $$U_w$$ to act on standard basis states $$|x\rangle$$ as $$U_w |x\rangle = (-1)^{f(x)}|x\rangle$$.

We see that if $$x$$ is an unmarked item, the oracle does nothing to the state (i.e. acts as identity). However, when we apply the oracle to the state $$|w\rangle$$, it maps $$U_w |w\rangle = -|w\rangle$$. Geometrically, this unitary matrix corresponds to a reflection about the origin for the marked item in an $$N=2^n$$-dimensional vector space as we saw in the lecture.

![fig2.png](/api/core/files/markdown/Markdown_2023-11-10T21-21-27-952_3d64be5e.png)

## The Grover Move

Before looking at the list of items, we have no idea where the marked item is. Therefore, any guess of its location is as good as any other. As previously, by applying the Hadamard transformation, we have created a state that encodes all function values (the whole truth table of $$f$$). 

$$|s\rangle = \frac{1}{\sqrt N}\sum_{x=0}^{N-1} |x\rangle $$

If at this point we were to measure in the standard basis $$|x\rangle$$, this superposition would collapse to any one of the basis states with the same probability of $$\frac{1}{N} = \frac{1}{2^{n}} $$. Therefore we get a uniformly random output, i.e. our chances of guessing the right value $$|w\rangle$$ is $$\frac{1}{2^{n}}$$, as could be expected. Hence, on average we would need to try about $$N=2^{n}$$ times to guess the correct item.

Now, let's recap the Grover move (also called amplitude amplification). We use the Boolean FT $$H$$ to switch to the fourier (XOR) basis, then slightly change the fourier coefficients and then switch back to the computational basis using the inverse of the BFT, $$H$$ again. Intuitively, this procedure amplifies the amplitude of the marked item, which shrinks the other items' amplitudes (as they need to sum to 1). Hence, measuring the final state will return the right item with near-certainty.

This algorithm has a nice geometrical interpretation in terms of two reflections, which generate a rotation in a two-dimensional euclidian plane. The only two special states we need to consider are the winner $$|w\rangle$$ and the uniform superposition $$|s\rangle$$. These two vectors span a two-dimensional plane in the vector space $$\mathbb C^{N}$$ . They are not quite perpendicular because $$|w\rangle$$ occurs in the superposition with amplitude $$N^{-1/2}$$ as well.

We can, however, introduce an additional state $$|s'\rangle$$ that is in the span of these two vectors, is perpendicular to $$|w\rangle$$, and is obtained from $$|s\rangle$$ by removing $$|w\rangle$$ and rescaling.

**Step 0:**

We start out in the uniform superposition $$|s\rangle$$. The uniform superposition is easily constructed from $$|s\rangle = H^{\otimes n}|0\rangle^{n}$$. At the beginning of the circuit (algorithm), the initial state is $$|\psi_{0}\rangle = |s\rangle$$.

![fig3.png](/api/core/files/markdown/Markdown_2023-11-10T21-28-08-261_3e3ce819.png)

**Step 1:** 

We apply the oracle reflection $$U_{w}$$ to the state $$U_{w}|\psi\_{t}\rangle = |\psi\_{t'}\rangle$$, which negates exactly one amplitude - the one of $$w$$. 

![fig4.png](/api/core/files/markdown/Markdown_2023-11-10T21-29-31-462_bfe73cb9.png)

Geometrically, this corresponds to a reflection of the state $$|\psi_{t}\rangle$$ about  $$|s'\rangle$$ . This transformation means that the amplitude in front of the $$|w\rangle$$ state becomes negative, which in turn means that the average amplitude has been lowered. (Note how the dotted line in the right graph is decreasing).

**Step 2**:

We now apply a reflection operator $$U_s = 2|s\rangle \langle s| - I$$ about the equal superposition state $$|s\rangle = H^{\otimes n}|0\rangle$$. This completes the Grover iteration:

$$|\psi_{t+1}\rangle = U_s U_w |\psi_t\rangle$$

To implement $$U_s$$ efficiently, we use the identity:

$$U_s = H^{\otimes n} (2|0\rangle\langle 0| - I) H^{\otimes n}$$

This corresponds to:
1. Applying Hadamard gates to move to the computational basis,
2. Flipping the phase of all basis states except $$|0\rangle^{\otimes n}$$,
3. Applying Hadamards again to return to the original basis.

This has the effect of reflecting the state about the average amplitude — amplifying the marked state(s) after each oracle call.

![fig5.png](/api/core/files/markdown/Markdown_2023-11-10T21-33-53-775_bb6675c0.png)

Two reflections always correspond to a rotation. The transformation $$ U_{s}U_{w}$$ rotates the initial state $$|s\rangle$$ closer toward the winner $$|w\rangle$$. Notice the left graph in Step 2. The action of the reflection $$U_{s}$$ in the amplitude bar diagram can be understood as a reflection about the average amplitude. Since the average amplitude has been lowered by the first reflection, this transformation boosts the negative amplitude of $$|w\rangle$$ to roughly three times its original value, while it decreases the other amplitudes. We then go to **Step１** to repeat the application. This procedure will be repeated several times to zero in on the winner. 

After $$t$$ steps, the state will have transformed to $$|\psi_{t}\rangle = (U_{s}U_{w})^{t}|\psi_{0}\rangle$$.

How many times do we need to apply the rotation? It turns out that roughly $$\lfloor\frac{\pi}{4}\sqrt N\rfloor$$ rotations suffice. This becomes clear when looking at the amplitudes of the state $$|\psi\_{t}\rangle$$ . We can see that the amplitude of $$|w\rangle$$ grows linearly with the number of applications（$$ \sim tN^{1/2}$$). Since we are dealing with amplitudes and not probabilities, the vector space's dimension enters as a square root. Therefore it is the amplitude, and not just the probability, that is being amplified in this procedure.

If there are multiple solutions, $$M$$, it can be shown that roughly $$\lfloor\frac{\pi}{4}\sqrt{(N/M)}\rfloor$$ rotations will suffice.

![fig6.png](/api/core/files/markdown/Markdown_2023-11-10T21-38-14-786_1bbce9c4.png)

With that, lets dive into the exercises!

_____________________________________

# Exercises

You can get a total of <span style="color:blue">**50 points**</span>
<br/>

## Exercise 1: Grover's algorithm using two qubits without auxiliary qubit

In this exercise, you will implement a simple Grover's algorithm using two qubits to search for the state $$\psi=|11\rangle$$.

[task][Exercise 1.1](test_ex1_init) - Initialize the quantum circuit with the correct number of qubits.

[task][Exercise 1.2](test_ex1_state_preparation) - Prepare the initial state of the quantum circuit.

[task][Exercise 1.3](test_ex1_oracle) - Apply the oracle for $$\psi=|11\rangle$$. This corresponds to a controlled-Z gate, as you can verify.

[task][Exercise 1.4](test_ex1_diffusion) - Apply the diffusion operator. As this is your first attempt in implementing a diffusion operator, refer to the circuit below for a possible implementation of the diffusion operator. Note that there are other implementation of a diffusion operator which you could experiment with.

![ex1_grover_2q_no_auxiliary_diffusion_operator.png](/api/core/files/markdown/Markdown_2023-11-11T14-29-53-945_c5b92f80.png)

[task][Exercise 1.5](test_ex1_grover_circuit) - Put the previously defined functions together to build a Grover circuit for one iteration (you do not need a for-loop).

[task][Exercise 1.6](test_ex1_simulate) - Simulate the circuit and return the <span style="color:blue">**statevector**</span>.

_____________________________________

## Exercise 2: Grover's Algorithm with more than 2 qubits using auxiliary qubits

In this exercise, you will implement Grover's algorithm with more than 2 qubits using auxiliary qubits for only **single solution**. A bit-string, also known as a binary string, is a sequence of bits, where each bit is a single digit and can be either 0 or 1, e.g: `10000`. We will search for bit-strings of length <span style="color:blue">**5**</span> in this exercise. 

Note that when you use auxiliary qubits, you don't need to "uncompute" the auxiliary qubits, i.e: apply the operations on the auxiliary qubits in reverse order at the end of the circuit.

[task][Exercise 2.1](test_ex2_init) - You will search for a <span style="color:blue">**5-bit string**</span> with the help of one qubit as auxiliary. Initialize the quantum circuit with the correct number of qubits in the query and auxiliary register.

[task][Exercise 2.2](test_ex2_state_preparation) - Prepare the initial state of the quantum circuit.

[task][Exercise 2.3](test_ex2_oracle) - You will be given an arbitrary bit-string as an argument `combination` in the function. Apply the oracle for the arbitrary bit-string. Use the multi-controlled X-gate from Qiskit for this exercise.

[task][Exercise 2.4](test_ex2_diffusion) - Apply the diffusion operator. As stated in Exercise 1, the diffusion operator can be different. For instance, you could use the auxiliary qubit to implement the diffusion operator.

[task][Exercise 2.5](test_ex2_grover_circuit) - Put the previously defined functions together to build a Grover circuit. Think about how many iterations you need to find the solution.

[task][Exercise 2.6](test_ex2_simulate) - Simulate the circuit and return the <span style="color:blue">**simulation counts**</span>. Remember to do `qc = qc.reverse_bits()` to reverse the bits **before** you write your code for simulation as Qiskit uses little-endian convention for qubit ordering in which the most significant bit (MSB) is placed on the left (with index $$0$$) while the least significant bit (LSB) is placed on the right (index $$n - 1$$). You can read more on Qiskit qubit ordering at [link](https://qiskit.org/documentation/explanation/endianness.html).

_____________________________________

## Exercise 3: Grover's Algorithm with more than 2 qubits using auxiliary qubits for multiple solutions 

In this exercise, you will implement Grover's algorithm with more than 2 qubits using auxiliary qubits for **multiple solution** for bit-strings of length <span style="color:blue">**5**</span>. You will be using functions implemented in Exercise 2 with modifications to the oracle and number of iterations needed to find the solutions. Specifically, the class in this exercise **inherits** from the class you implemented in Exercise 2. We will only override the `oracle` and `grover_circuit` function. Therefore, note that you need to **complete Exercise 2 before you can work on this exercise**.

[task][Exercise 3.1](test_ex3_oracle) - You will be given an arbitrary bit-string**s** as an argument `combinations` which has type `list[str]` in the function. Apply the oracle for the every arbitrary bit-string in the list. Use the multi-controlled X-gate from Qiskit for this exercise.

[task][Exercise 3.2](test_ex3_grover_circuit) - The functions defined in Exercise 2 are available for you as you have just inherited from the class defined in Exercise 2. Put together these functions and the `oracle` function you did in Exercise 3.1 to build a Grover circuit. Think about how many iterations you need to find the solution. You can calculate the number of iterations needed by using the number of combinations given to you in the `combinations` argument.

_____________________________________

## Exercise 4: Fun With A Small Puzzle

In this exercise, you will solve a little puzzle game with the help of Grover's algorithm. 

You are given a rectangular grid of "lights" (Boolean values) which can be switched on and off. When you flip a switch inside one of those squares, it will toggle the on/off state of this and adjacent squares (up, down, left and right). Your goal is, given a random starting pattern, to turn all the lights off.

### Example Puzzle

An example of the puzzle with 3 x 3 grid is shown in the figure below. The light squares are labelled from 0 to 8. We can represent the starting pattern using a list of numbers, where `1` represents lights switched on and `0` represnts ligths switched off. The list `lights` below represents the starting pattern in this example (squares 3, 5, 6, 7 are on and the rest are off):

```python
state_of_lights = [0, 0, 0, 1, 0, 1, 1, 1, 0]
```

The example puzzle can be solved by flipping the switches in square 0, 3 and 4 as illustrated step by step in the figure. If you play with it a little bit, you will soon notice **two important properties of this puzzle game**:

1. You don't need to flip a switch more than once.
2. The order of flipping doesn't matter.

Therefore, we can represent the puzzle solution as a list of numbers similar to the starting pattern. However, the meaning of `0` and `1` are different here:  `1` represents flipping a switch and `0` represents *not* flipping a switch. 

```python
solution = [1, 0, 0, 1, 1, 0, 0, 0, 0]
```

![ex4_3_3_tile.png](/api/core/files/markdown/Markdown_2023-11-11T14-46-31-887_d7766275.png)

To make your life a little easier, lets focus on a simpler case, where we are given a $$2\times2$$ tiling.

### $$2\times2$$ Puzzle

An example of a starting board with $$2\times2$$ tiling is as below:

![ex4_2_2_tile.png](/api/core/files/markdown/Markdown_2023-11-11T14-49-02-283_459d9ebd.png)

The corresponding boolean list representing the board in the image is $$[0, 0, 1, 1]$$. While in the previous case the "winning state" was given as a binary vector, this problem is conceptually a bit more complex to model. The winning state is a pattern of light flipping that results in **all lights being turned off**.

The overall circuit we want to build looks something like following:

![ex4_circuit_schematic.jpeg](/api/core/files/markdown/Markdown_2023-11-11T14-53-34-649_8b090af3.jpeg)

[task][Exercise 4.1](test_ex4_init) - Initialize the quantum circuit with the correct number of qubits in the query (flip and tile) registers and auxiliary register as well as number of classical bits in the classical register. For the classical bits, think about which quantum register (flip, tile, or auxiliary) do you want to measure and store the result in the classical register.

[task][Exercise 4.2](test_ex4_state_preparation) - Prepare the initial state of the quantum circuit. 

1. Create equal superposition (Hadamard transform) in the `flip` register. This represents candidates of solution. Remember this as it will be useful when you calculate the number of iterations needed to find the solution.
2. You should map the board's current state on the `tile` register
3. Initializes the auxiliary qubit (which marks the solution that turns every tile off) result in its phase.

[task][Exercise 4.3](test_ex4_oracle) - Apply the oracle for to find the solution. The oracle can be split into 3 parts.

1. "Flipping" logic. The following image shows the "flipping" logic. For example, if you push $$0$$, $$[0,1,2]$$ flips from its current state. Hint: You need to use CX gates connecting the `flip` register to the `tile` register to encode this logic.

![ex4_flip_logic.png](/api/core/files/markdown/Markdown_2023-11-11T14-57-23-904_b5032af1.png)

2. "Light check" logic to check if all lights are turned off. Use the multi-controlled X-gate from Qiskit. Remember, you are checking whether all lights are turned off, meaning they are in the $$0$$ state and the multi-controlled X-gate flips the state if its control qubits are in the $$1$$ state, so you need to sandwich the multi-controlled gate between a sequence of gates.
3. Apply "Flipping" logic in (1) again to make the subroutine reversible.

[task][Exercise 4.4](test_ex4_diffusion) - Apply the diffusion operator. As you may have seen in previous exercises, the diffusion operator can be different. However, for this exercise, implement the diffusion operator using multi-controlled X-gate from Qiskit and without using the auxiliary qubit.

[task][Exercise 4.5](test_ex4_grover_circuit) - Put the previously defined functions together to build a Grover circuit. Think about how many iterations you need to find the solution. You can assume there is only one solution.

[task][Exercise 4.6](test_ex4_simulate) - Simulate the circuit and return the <span style="color:blue">**simulation counts**</span>. Remember to reverse the bits **before** you write your code for simulation.

_____________________________________

## Exercise 5: Kakuro

Kakuro, a cross-sum riddle, is composed of a grid structure with $$M$$ rows and $$N$$ columns, where each row and column shall add up to a given sum. Additionally, numbers within each row and each column must be distinct. 

In this exercise, we will solve a simple Kakuro riddle instantiation with a grid structure of $$2\times2$$ as shown below, where the goal is to determine $$a$$, $$b$$, $$c$$, and $$d$$ such that the respective sums add up to $$1$$. 

![ex5_kakuro_2_2.png](/api/core/files/markdown/Markdown_2023-11-11T15-04-12-758_649e842d.png)

Thus, all those variables are to be assigned either $$0$$ or $$1$$. A solution to this problem is characterized by satisfying the constraints $$a \neq b$$, $$b \neq d$$, and $$c \neq d$$.

[task][Exercise 5.1](test_ex5_init) - Initialize number of qubits and classical bits required.

[task][Exercise 5.2](test_ex5_state_preparation) - Do state preparation.

[task][Exercise 5.3](test_ex5_oracle) - Implement the oracle for the $$2\times2$$ Kakuro riddle. Note that your oracle needs to <span style="color:blue">**encode the constraints**</span> $$a \neq b$$, $$b \neq d$$, and $$c \neq d$$. Do not hardcode the working combination in the oracle as then, the test won't pass.

[task][Exercise 5.4](test_ex5_diffusion) - Implement the diffusion operator for the $$2\times2$$ Kakuro riddle.

[task][Exercise 5.5](test_ex5_grover_circuit) - Put the functions together to build a Grover circuit.

[task][Exercise 5.6](test_ex5_simulate) - Simulate the circuit and return the <span style="color:blue">**simulation counts**</span>. Remember to reverse the bits **before** you write your code for simulation.

_____________________________________

In the final part of this lab, we explore one of the most fundamental quantum algorithms: the Quantum Fourier Transform (QFT). The QFT is the quantum analogue of the classical discrete Fourier transform and plays a crucial role in several quantum algorithms, such as Shor’s algorithm for integer factorization.

In Exercise 6, we begin with a manual implementation of the QFT for 3 qubits, following a specific circuit diagram. This helps build intuition for how Hadamard and controlled-phase gates work together to transform quantum amplitudes into their frequency-domain representation. We also implement the inverse QFT, which undoes the transformation and is often used at the end of algorithms to recover results in the computational basis.

In Exercise 7, we generalize our implementation to an arbitrary number of qubits, constructing both the forward and inverse QFT dynamically for any given circuit. This reinforces your understanding of recursive quantum circuit design and prepares you to apply the QFT flexibly in more complex algorithms.

## Exercise 6: Quantum Fourier Transform (QFT) for 3 qubits

**Qubit ordering: $$q\_{0}\otimes\dots \otimes q\_{n-1}$$**

For this exercise, **do not** use the QFT module from Qiskit.

[task][Exercise 6.1](test_ex1_qft_circuit) - Implement QFT for 3 qubits as following circuit diagram: 

![qft_3_qubit.png](/api/core/files/markdown/Markdown_2023-11-18T19-37-59-625_bd344683.png)

[task][Exercise 6.2](test_ex1_qft_circuit_inverse) - Implement the **inverse** QFT for 3 qubits. Hint: You can reuse the circuit built in Exercise 1.1 if you want to.

______________________________

# Exercise 7: Quantum Fourier Transform (QFT) for arbitrary number of qubits

**Qubit ordering: $$q\_{0}\otimes\dots \otimes q\_{n-1}$$**

For this exercise, **do not** use the QFT module from Qiskit. You are only given the Quantum Circuit as argument to the functions in these exercises.

[task][Exercise 7.1](test_ex2_qft_circuit_n_qubits) Implement QFT on the given Quantum Circuit.

[task][Exercise 7.2](test_ex2_qft_circuit_n_qubits_inverse) Implement the **inverse** QFT on the given Quantum Circuit. Hint: You can reuse the circuit built in Exercise 2.1 if you want to.

And that's all for this lab. Well done!
_____________________________________