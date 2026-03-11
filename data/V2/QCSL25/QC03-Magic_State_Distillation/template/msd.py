from __future__ import annotations
import numpy as np
import stim
import matplotlib.pyplot as plt
import numpy.typing as npt


# X checks of the [[15,1,3]] code
hx_tetrahedral = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                           [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]])

# Z checks of the [[15,1,3]] code
hz_tetrahedral = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                           [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1]])


def construct_zero_state_prep_circuit(Hx: npt.NDArray[np.int8], offset:int=0) -> stim.Circuit:
    """
    Constructs a state preparation Stim circuit from the X-check matrix of a CSS code.

    Parameters:
        Hx (npt.NDArray[np.int8]): The X-check matrix of the CSS code.
        offset (int): The offset to apply to the qubit indices in the circuit.

    Returns:
        stim.Circuit: A Stim circuit that prepares the logical zero state on qubits [offset, offset+nq-1] where nq is the number of physical qubits of the code.
    """
    raise NotImplementedError("construct_zero_state_prep_circuit is not implemented.")


def make_y_state(circ: stim.Circuit, q: int, p: float) -> None:
    """Prepare a noisy |Y> state on the specified qubit.

    Args:
        circ (stim.Circuit): The circuit to append the operations to.
        q (int): The qubit index where the |Y> state will be prepared.
        p (float): The depolarization probability for simulating noise.
    """
    raise NotImplementedError("make_y_state is not implemented.")


def inject(circ: stim.Circuit, data_qubit: int, injection_qubit) -> int:
    """Construct the injection circuit for teleporting a gate from an ancilla qubit to a data qubit.

    Args:
        circ (stim.Circuit): The circuit to append the injection operations to.
        data_qubit (int): The qubit where the data is injected.
        injection_qubit (int): The ancilla qubit that will receive the data.

    Returns:
        int: The index of the measurement operation that will be used to inject the data.
    """
    raise NotImplementedError("inject is not implemented.")

def correct_teleportation(teleportation_measurements: npt.NDArray[np.int8], x_measurements: npt.NDArray[np.int8]) -> npt.NDArray[np.int8]:
    """Correct the teleportation measurements based on the |Y> state measurements.

    Args:
        teleportation_measurements (npt.NDArray[np.int8]): An array of measurements from mutliple teleportations.
        x_measurements (npt.NDArray[np.int8]): An array of X-basis measurements of the qubit the gate was teleported to.

    Returns:
        npt.NDArray[np.int8]: An array of corrected measurements.
    """
    raise NotImplementedError("correct_teleportation is not implemented.")


def teleport_s(circ: stim.Circuit, data_qubit: int, injection_qubit: int, p = 0.0) -> int:
    """Construct the circuit for teleporting an S gate from an ancilla qubit to a data qubit.

    Args:
        circ (stim.Circuit): The circuit to append the teleportation operations to.
        data_qubit (int): The qubit where the S gate will be teleported to.
        injection_qubit (int): The ancilla qubit to be prepared in the |Y> state.
        p (float): The depolarization probability for simulating noise.

    Returns:
        int: The index of the measurement operation that will be used to inject the data.
    """
    raise NotImplementedError("teleport_s is not implemented.")


def build_msd_circ(circ: stim.Circuit, distilled_state: int, y_states:list[int]) -> tuple[list[int], list[int]]:
    """Build the circuit for the S-MSD protocol.

    Args:
        circ (stim.Circuit): The circuit to append the operations to.
        distilled_state (int): The qubit index where the distilled state will be stored.
        y_states (list[int]): A list of qubit indices use for the |Y> resource states.

    Returns:
        tuple[list[int], list[int]]: A tuple containing two lists:
            - The indices of the measurement operations used for teleportation.
            - The indices of the final $X$-basis measurements of the distilled state.
    """
    raise NotImplementedError("build_msd_circ is not implemented.")


def detect_errors(measurements: npt.NDArray[np.int8], checks: npt.NDArray[np.int8]) -> npt.NDArray[np.int8]:
    """Detect errors in the measurements based on the provided checks.

    Args:
        measurements (npt.NDArray[np.int8]): An array of measurements from multiple shots.
        checks (npt.NDArray[np.int8]): The check matrix used to detect errors.
    Returns:
        npt.NDArray[np.int8]: An array indicating which shots are good (1) or have errors (0).
    """
    raise NotImplementedError("detect_errors is not implemented.")


def simulate_msd_one_round(n_shots: int, p: float) -> tuple[float, float]:
    """Simulate one round of the |Y> state distillation protocol.

    Args:
        n_shots (int): The number of shots to simulate.
        p (float): The depolarization probability for simulating noise.

    Returns:
        tuple[float, float]: A tuple containing the error rate and acceptance rate estimates of the protocol.
    """
    raise NotImplementedError("simulate_msd_one_round is not implemented.")


def simulate_msd_two_rounds(n_shots: int, p: float, batch_size: int = 1000000) -> tuple[float, float]:
    """
    Simulate two rounds of the |Y> state distillation protocol in batches.

    Args:
        n_shots (int): Total number of shots to simulate.
        p (float): Depolarization probability for simulating noise.
        batch_size (int): Number of shots to process in each batch.

    Returns:
        tuple[float, float]: A tuple containing the error rate and acceptance rate estimates of the protocol.
    """
    raise NotImplementedError("simulate_msd_two_rounds is not implemented.")
    
def plot_msd(ps: list[float], n_shots=1000):
    """
    Plot the error rate and acceptance rate of the S-MSD protocol for different depolarization probabilities,
    along with the theoretical p^3 scaling curve for comparison.
    """

    # Simulate the MSD protocol for each depolarization probability
    results = [simulate_msd_one_round(p=p, n_shots=n_shots) for p in ps]
    error_rates = [r[0] for r in results]
    acceptance_rates = [r[1] for r in results]

    # Theoretical p^3 scaling curve
    p_cubed = [35 / 3 * p**3 for p in ps]

    # Create the plot
    plt.figure(figsize=(12, 6))

    # Plot error rates
    plt.plot(ps, error_rates, marker='o', label='Simulated MSD Error', color='blue')

    # Plot acceptance rates
    plt.plot(ps, acceptance_rates, marker='x', label='Acceptance Rate', color='green')

    # Plot theoretical p^3 scaling
    plt.plot(ps, p_cubed, linestyle='--', label='$p^3$ scaling', color='red')

    # Add labels, title, and legend
    plt.xlabel('Depolarization Probability (p)')
    plt.ylabel('Rate')
    plt.title('Error and Acceptance Rates of 15-to-1 Magic State Distillation vs Depolarization Probability')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which='both', ls=':')
    plt.legend()

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()


def plot_msd_two_rounds(ps: list[float], n_shots=1000):
    """
    Plot the error rate and acceptance rate of the S-MSD protocol for different depolarization probabilities,
    along with the theoretical p^3 scaling curve for comparison.
    """

    # Simulate the MSD protocol for each depolarization probability
    results = [simulate_msd_two_rounds(p=p, n_shots=n_shots) for p in ps]
    error_rates = [r[0] for r in results]
    print(error_rates)
    acceptance_rates = [r[1] for r in results]

    # Theoretical p^3 scaling curve
    p_cubed = [35/3*(35 / 3 * p**3)**3 for p in ps]

    # Create the plot
    plt.figure(figsize=(12, 6))

    # Plot error rates
    plt.plot(ps, error_rates, marker='o', label='Simulated MSD Error', color='blue')

    # Plot acceptance rates
    plt.plot(ps, acceptance_rates, marker='x', label='Acceptance Rate', color='green')

    # Plot theoretical p^3 scaling
    plt.plot(ps, p_cubed, linestyle='--', label='$p^3$ scaling', color='red')

    # Add labels, title, and legend
    plt.xlabel('Depolarization Probability (p)')
    plt.ylabel('Rate')
    plt.title('Error and Acceptance Rates of 15-to-1 Magic State Distillation vs Depolarization Probability')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which='both', ls=':')
    plt.legend()

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()
    
    
