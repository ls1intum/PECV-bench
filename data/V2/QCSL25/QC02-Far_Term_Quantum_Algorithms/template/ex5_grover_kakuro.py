from __future__ import annotations
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram
import numpy as np


class GroverKakuro:
    def __init__(self):
        """Exercise 5.1: Initialize the quantum circuit with the correct number of qubits
        
        Think about how many qubits you need to represent all possible 2x2 Kakuro combinations 
        (assume binary values 0 or 1 per cell, one qubit per cell) and what’s required for Grover’s algorithm to function properly.
        Use a minimal number of qubits for the auxiliary register and enough classical bits to read out 
        the state of your solution candidates.
        
        """
        self.number_of_qubits_query_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_qubits_auxiliary_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_bits_classical_register = 0  ### FILL IN NUMBER OF BITS ###
        self.query_register = QuantumRegister(
            self.number_of_qubits_query_register, name="query_register"
        )
        self.auxiliary_register = QuantumRegister(
            self.number_of_qubits_auxiliary_register, name="auxiliary_register"
        )
        self.classical_register = ClassicalRegister(
            self.number_of_bits_classical_register, name="classical_register"
        )
        self.qc = QuantumCircuit(
            self.query_register, self.auxiliary_register, self.classical_register
        )

    def state_preparation(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 5.2: Prepare the initial state of the quantum circuit

        Prepare a uniform superposition over all valid candidate states in the query register.
        Don’t forget to set the auxiliary qubit into the appropriate state for phase kickback to work later.

        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
        """
        pass

    def oracle(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 5.3: Apply the oracle for the 2 x 2 Kakuro riddle

        The oracle should flip the phase of the state(s) that represent correct Kakuro solutions.
        Consider how to encode constraints (e.g., sums of rows and columns) using quantum logic gates.
        Use multi-controlled operations as necessary.

        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
        """
        pass

    def diffusion(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 5.4: Apply the diffusion operator for the 2 x 2 Kakuro riddle

        Amplify the probability of the marked state(s). Implement an inversion about the average
        on the query register only. Think carefully about how to adapt the standard diffusion pattern 
        to your number of qubits.

        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
        """
        pass

    def grover_circuit(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
        classical_register: ClassicalRegister,
    ) -> QuantumCircuit:
        """Exercise 5.5: Put the previously defined functions together to build a Grover circuit

        Use your previous components (state preparation, oracle, diffusion) to build the 
        Grover search circuit. Apply the Grover iteration the correct number of times for 
        a single marked item in a space of 2ⁿ possible states.

        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
        """
        pass

    def simulate(self, qc: QuantumCircuit) -> dict[str, int]:
        """Exercise 5.6: Simulate the circuit and return the counts

        Run the circuit on a simulator and return a histogram of measured outcomes.
        Make sure your measurement is correctly set up to extract meaningful information
        from the query register.

        Args:
            qc: The quantum circuit
            query_register: The quantum register
        """
        pass

    def run(self) -> dict[str, int]:
        """If you want to test your code in a Jupyter notebook, you can run this function
        to see the result of your implementation
        grover = Kakuro()
        grover.run()
        """
        self.qc = self.grover_circuit(
            self.qc,
            self.query_register,
            self.auxiliary_register,
            self.classical_register,
        )
        print(self.qc.draw("text"), "\n")
        counts = self.simulate(self.qc)
        display(plot_histogram(counts))
        return counts
