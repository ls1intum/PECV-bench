from __future__ import annotations
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram
import numpy as np


class GroverMultiQubitWithAuxiliaryQubit:
    def __init__(self):
        """Exercise 2.1: Initialize the quantum circuit with the correct number of qubits"""
        self.number_of_qubits_query_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_qubits_auxiliary_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.query_register = QuantumRegister(
            self.number_of_qubits_query_register, name="query_register"
        )
        self.auxiliary_register = QuantumRegister(
            self.number_of_qubits_auxiliary_register, name="auxiliary_register"
        )
        self.classical_register = ClassicalRegister(
            self.number_of_qubits_query_register, name="classical_register"
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
        """Exercise 2.2: Prepare the initial state of the quantum circuit
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
        combination: str,
    ) -> QuantumCircuit:
        """Exercise 2.3: You will be given an arbitrary bit-string as an argument `combination`
        in the function. Apply the oracle for the arbitrary bit-string.
        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
            combination: The bit-string to be searched
        """
        pass

    def diffusion(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 2.4: Apply the diffusion operator. As stated in Exercise 1, the diffusion operator
        can be different. For instance, you could use the auxiliary qubit to implement the diffusion operator.
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
        combination: str,
    ) -> QuantumCircuit:
        """Exercise 2.5: Put the previously defined functions together to build a Grover circuit
        Args:
            qc: The quantum circuit
            query_register: The quantum register
            auxiliary_register: The auxiliary register
            classical_register: The classical register
            combination: The bit-string to be searched
        """
        pass

    def simulate(self, qc: QuantumCircuit) -> dict[str, int]:
        """Exercise 2.6: Simulate the circuit and return the simulation counts
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def run(self) -> dict[str, int]:
        """If you want to test your code locally in a Jupyter notebook, you can run this function
        to see the result of your implementation
        grover = GroverMultiQubitWithAuxiliaryQubit()
        grover.run()
        """
        combination = "10000"
        self.qc = self.grover_circuit(
            self.qc,
            self.query_register,
            self.auxiliary_register,
            self.classical_register,
            combination,
        )
        print(self.qc.draw("text"), "\n")
        counts = self.simulate(self.qc)
        display(plot_histogram(counts))
        return counts
