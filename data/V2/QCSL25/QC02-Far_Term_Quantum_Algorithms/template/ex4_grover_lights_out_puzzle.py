from __future__ import annotations
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram
import numpy as np


class GroverLightsOutPuzzle:
    def __init__(self):
        """Exercise 4.1: Initialize the quantum circuit with the correct number of qubits
        in the query (flip and tile) registers and auxiliary register"""
        self.number_of_qubits_flip_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_qubits_tile_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_qubits_auxiliary_register = 0  ### FILL IN NUMBER OF QUBITS ###
        self.number_of_bits_classical_register = 0  ### FILL IN NUMBER OF BITS ###
        self.flip_register = QuantumRegister(
            self.number_of_qubits_flip_register, name="flip_register"
        )
        self.tile_register = QuantumRegister(
            self.number_of_qubits_tile_register, name="tile_register"
        )
        self.auxiliary_register = QuantumRegister(
            self.number_of_qubits_auxiliary_register, name="auxiliary_register"
        )
        self.classical_register = ClassicalRegister(
            self.number_of_bits_classical_register, name="classical_register"
        )
        self.qc = QuantumCircuit(
            self.flip_register,
            self.tile_register,
            self.auxiliary_register,
            self.classical_register,
        )

    def state_preparation(
        self,
        qc: QuantumCircuit,
        flip_register: QuantumRegister,
        tile_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
        state_of_lights: list[int],
    ) -> QuantumCircuit:
        """Exercise 4.2: Prepare the initial state of the quantum circuit
        Args:
            qc: The quantum circuit
            flip_register: The flip register
            tile_register: The tile register
            auxiliary_register: The auxiliary register
            state_of_lights: The state of the lights
        """
        pass

    def oracle(
        self,
        qc: QuantumCircuit,
        flip_register: QuantumRegister,
        tile_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 4.3: Apply the oracle for the 2 x 2 Kakuro riddle
        Args:
            qc: The quantum circuit
            flip_register: The flip register
            tile_register: The tile register
            auxiliary_register: The auxiliary register
        """
        pass

    def diffusion(
        self,
        qc: QuantumCircuit,
        flip_register: QuantumRegister,
    ) -> QuantumCircuit:
        """Exercise 4.4: Apply the diffusion operator
        Args:
            qc: The quantum circuit
            flip_register: The flip register
        """
        pass

    def grover_circuit(
        self,
        qc: QuantumCircuit,
        flip_register: QuantumRegister,
        tile_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
        classical_register: ClassicalRegister,
        state_of_lights: list[int],
    ) -> QuantumCircuit:
        """Exercise 4.5: Put the previously defined functions together to build a Grover circuit
        Args:
            qc: The quantum circuit
            flip_register: The flip register
            tile_register: The tile register
            auxiliary_register: The auxiliary register
            classical_register: The classical register
            state_of_lights: The state of the lights
        """
        pass

    def simulate(self, qc: QuantumCircuit) -> dict[str, int]:
        """Exercise 4.6: Simulate the circuit and return the counts
        Args:
            qc: The quantum circuit
            query_register: The quantum register"""
        pass

    def run(self) -> dict[str, int]:
        """If you want to test your code locally in a Jupyter notebook, you can run this function
        to see the result of your implementation
        grover = GroverLightsOutPuzzle()
        grover.run()
        """
        self.qc = self.grover_circuit(
            self.qc,
            self.flip_register,
            self.tile_register,
            self.auxiliary_register,
            self.classical_register,
            state_of_lights=[0, 0, 1, 1],
        )
        print(self.qc.draw("text"), "\n")
        counts = self.simulate(self.qc)
        display(plot_histogram(counts))
        return counts
