from __future__ import annotations
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.quantum_info import Statevector
import numpy as np


class GroverTwoQubitWithoutAuxiliaryQubit:
    def __init__(self):
        """Exercise 1.1: Initialize the quantum circuit with the correct number of qubits"""
        self.number_of_qubits_query_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.query_register = QuantumRegister(self.number_of_qubits_query_register)
        self.qc = QuantumCircuit(self.query_register)

    def state_preparation(
        self, qc: QuantumCircuit, query_register: QuantumRegister
    ) -> QuantumCircuit:
        """Exercise 1.2: Prepare the initial state of the quantum circuit
        Args:
            qc: The quantum circuit
            query_register: The quantum register
        """
        pass

    def oracle(
        self, qc: QuantumCircuit, query_register: QuantumRegister
    ) -> QuantumCircuit:
        """Exercise 1.3: Apply the oracle for Ψ=|11>
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def diffusion(
        self, qc: QuantumCircuit, query_register: QuantumRegister
    ) -> QuantumCircuit:
        """Exercise 1.4: Apply the diffusion operator
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def grover_circuit(
        self, qc: QuantumCircuit, query_register: QuantumRegister
    ) -> QuantumCircuit:
        """Exercise 1.5: Put the previously defined functions together to build a Grover circuit
          for one iteration (no need for-loop)
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def simulate(self, qc: QuantumCircuit) -> list[complex]:
        """Exercise 1.6: Simulate the circuit and return the statevector
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def run(self):
        """If you want to test your code locally, you can run this function
        to see the result of your implementation
        grover = GroverTwoQubitWithoutAuxiliaryQubit()
        grover.run()
        """
        self.qc = self.grover_circuit(self.qc, self.query_register)
        print(self.qc.draw("text"), "\n")
        outputstate = self.simulate(self.qc)
        print(f"Ψ: {outputstate}")
