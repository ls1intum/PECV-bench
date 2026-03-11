from __future__ import annotations
from qiskit import QuantumCircuit
import numpy as np


class QFT3Qubit:
    def __init__(self):
        self.qc = QuantumCircuit(3)

    def qft_circuit(self, qc: QuantumCircuit) -> QuantumCircuit:
        """
        Exercise 1.1: Implement QFT for 3 qubits.

        Args:
            qc (QuantumCircuit): quantum circuit

        Returns:
            QuantumCircuit: qunatum circuit with QFT
        """
        pass

    def qft_circuit_inverse(self, qc: QuantumCircuit) -> QuantumCircuit:
        """Exercise 1.2: Implement the inverse QFT for 3 qubits

        Args:
            qc (QuantumCircuit): Quantum circuit

        Returns:
            QuantumCircuit: Quantum circuit
        """
        pass
