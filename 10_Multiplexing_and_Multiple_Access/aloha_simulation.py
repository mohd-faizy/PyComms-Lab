"""Pure and Slotted ALOHA Multiple Access Throughput.

Simulates and compares the throughput of Pure ALOHA and Slotted ALOHA systems
as a function of offered channel traffic load (G), verifying the theoretical
max limits of 18.4% and 36.8% respectively.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_pure_aloha(g_load, sim_time=10000):
    """Simulate Pure ALOHA channel.

    g_load: average number of packets generated per packet duration Tp (Tp=1)
    """
    # Packet arrival modeled as a Poisson process
    # Time between arrivals is exponentially distributed with mean 1/g_load
    arrivals = []
    t = 0.0
    while t < sim_time:
        t += np.random.exponential(1.0 / g_load)
        if t < sim_time:
            arrivals.append(t)
            
    n_packets = len(arrivals)
    if n_packets == 0:
        return 0.0

    successful_packets = 0
    # A packet at index i is successful if no other packet is transmitted
    # in the interval [t_i - 1, t_i + 1] (vulnerable period is 2*Tp)
    for i in range(n_packets):
        t_curr = arrivals[i]
        
        # Check if there is collision with previous packet
        collision = False
        if i > 0 and (t_curr - arrivals[i - 1]) < 1.0:
            collision = True
        # Check if there is collision with next packet
        if i < n_packets - 1 and (arrivals[i + 1] - t_curr) < 1.0:
            collision = True
            
        if not collision:
            successful_packets += 1

    throughput = successful_packets / sim_time
    return throughput


def simulate_slotted_aloha(g_load, num_slots=10000):
    """Simulate Slotted ALOHA channel.

    g_load: average number of packets generated per slot (Tp=1 slot)
    """
    # Number of packets arriving in each slot follows a Poisson distribution
    # with mean g_load.
    arrivals_per_slot = np.random.poisson(g_load, num_slots)
    
    # A slot is successful if exactly 1 packet arrives in that slot
    successful_slots = np.sum(arrivals_per_slot == 1)
    
    throughput = successful_slots / num_slots
    return throughput


def main():
    g_loads = np.logspace(-2.3, 1.0, 40)  # Load range from ~0.005 to 10
    pure_sim = []
    slotted_sim = []

    np.random.seed(42)

    for g in g_loads:
        pure_sim.append(simulate_pure_aloha(g))
        slotted_sim.append(simulate_slotted_aloha(g))

    # Theoretical curves
    g_theory = np.logspace(-2.5, 1.2, 200)
    pure_theory = g_theory * np.exp(-2.0 * g_theory)
    slotted_theory = g_theory * np.exp(-g_theory)

    plt.figure(figsize=(9.5, 6))
    
    # Theoretical lines
    plt.plot(g_theory, pure_theory, "-", label="Theoretical Pure ALOHA", color="r", linewidth=2)
    plt.plot(g_theory, slotted_theory, "-", label="Theoretical Slotted ALOHA", color="c", linewidth=2)

    # Simulated points
    plt.plot(g_loads, pure_sim, "o", label="Simulated Pure ALOHA", color="r", markersize=6)
    plt.plot(g_loads, slotted_sim, "s", label="Simulated Slotted ALOHA", color="gray", markersize=6)

    # Highlight Maximum throughput lines
    plt.axhline(1 / (2 * np.e), color="r", linestyle=":", alpha=0.7)
    plt.axvline(0.5, color="r", linestyle=":", alpha=0.7)
    plt.text(0.52, 0.16, "Max: 18.4% at G=0.5", color="r", fontsize=9, fontweight="bold")

    plt.axhline(1 / np.e, color="c", linestyle=":", alpha=0.7)
    plt.axvline(1.0, color="c", linestyle=":", alpha=0.7)
    plt.text(1.02, 0.33, "Max: 36.8% at G=1.0", color="gray", fontsize=9, fontweight="bold")

    plt.xscale("log")
    plt.title("ALOHA Multiple Access Protocol: Throughput vs. Offered Load", fontsize=13, fontweight="bold")
    plt.xlabel("Offered Channel Load G (packets / packet time)")
    plt.ylabel("Normalized Throughput S (packets / packet time)")
    plt.xlim(0.01, 10.0)
    plt.ylim(0.0, 0.45)
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print("=== ALOHA Simulation Results Summary ===")
    print(f"{'Offered Load G':<15} | {'Pure ALOHA (Sim)':<20} | {'Slotted ALOHA (Sim)':<20}")
    print("-" * 65)
    for target in [0.1, 0.5, 1.0, 2.0]:
        idx = np.argmin(np.abs(g_loads - target))
        print(f"{g_loads[idx]:<15.2f} | {pure_sim[idx]:<20.4f} | {slotted_sim[idx]:<20.4f}")


if __name__ == "__main__":
    main()
