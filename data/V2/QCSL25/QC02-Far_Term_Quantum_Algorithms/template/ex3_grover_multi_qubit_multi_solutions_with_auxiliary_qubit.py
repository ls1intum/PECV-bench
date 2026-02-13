from __future__ import annotations
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram
import numpy as np
from .ex2_grover_multi_qubit_with_auxiliary_qubit import (
    GroverMultiQubitWithAuxiliaryQubit,
)


class GroverMultiQubitMultiSolutionsWithAuxiliaryQubit(
    GroverMultiQubitWithAuxiliaryQubit
):
    def __init__(self):
        super().__init__()

    def oracle(
        self,
        qc: QuantumCircuit,
        query_register: QuantumRegister,
        auxiliary_register: QuantumRegister,
        combinations: list[str],
    ) -> QuantumCircuit:
        """Exercise 3.1: You will be given an arbitrary list of bit-string as an argument `combinations`
        in the function. Apply the oracle for the arbitrary list of bit-string.
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
        combinations: list[str],
    ) -> QuantumCircuit:
        """Exercise 3.2: The functions defined in Exercise 2 are available for you as we have just
        inherited from the class defined in Exercise 2. Put together these functions and the `oracle`
        function you did in Exercise 3.1 to build a Grover circuit. Think about how many iterations you
        need to find the solution. You can calculate the number of iterations needed by using the number of
        combinations given to you in the `combinations` argument.
        Args:
            qc: The quantum circuit
            query_register: The quantum registe
            auxiliary_register: The auxiliary register
            classical_register: The classical register
            combinations: The list of bit-strings to be searched
        """
        pass

    def run(self) -> dict[str, int]:
        """If you want to test your code locally in a Jupyter notebook, you can run this function
        to see the result of your implementation
        grover = GroverMultiQubitMultiSolutionsWithAuxiliaryQubit()
        grover.run()
        """
        combination = ["01000", "10000"]
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
