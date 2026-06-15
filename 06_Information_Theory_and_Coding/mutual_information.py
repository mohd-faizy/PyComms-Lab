"""Mutual Information and BSC Channel Capacity.

Simulates and visualises the mutual information I(X;Y) of a Binary Symmetric
Channel (BSC) as a function of crossover probability 'p' and source distribution 'q'.
"""

import numpy as np
import matplotlib.pyplot as plt


def binary_entropy(p):
    """Compute binary entropy H(p) in bits."""
    p = np.clip(p, 1e-12, 1.0 - 1e-12)
    return -p * np.log2(p) - (1.0 - p) * np.log2(1.0 - p)


def bsc_mutual_information(q, p):
    """Compute mutual information I(X;Y) for BSC.

    q = P(X=1) (source probability)
    p = channel crossover probability
    """
    # Entropy of the source H(X)
    h_x = binary_entropy(q)

    # Probability of output Y
    # P(Y=1) = P(Y=1|X=1)*P(X=1) + P(Y=1|X=0)*P(X=0)
    # P(Y=1) = (1-p)*q + p*(1-q)
    py1 = (1.0 - p) * q + p * (1.0 - q)
    h_y = binary_entropy(py1)

    # Conditional entropy H(Y|X)
    # H(Y|X) = q*H(Y|X=1) + (1-q)*H(Y|X=0)
    # Since H(Y|X=1) = H(p) and H(Y|X=0) = H(p), H(Y|X) = H(p)
    h_y_given_x = binary_entropy(p)

    # Mutual Information I(X;Y) = H(Y) - H(Y|X)
    i_xy = h_y - h_y_given_x
    return i_xy


def main():
    q_vals = np.linspace(0, 1, 200)
    p_vals = np.linspace(0, 0.5, 200)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Mutual Information vs Source Probability q ---
    p_targets = [0.0, 0.05, 0.1, 0.2, 0.5]
    colors = ["gray", "c", "gray", "orange", "r"]
    
    for p, col in zip(p_targets, colors):
        mi = [bsc_mutual_information(q, p) for q in q_vals]
        ax1.plot(q_vals, mi, label=f"p = {p:.2f} (crossover)", color=col, linewidth=2)

    ax1.set_title("Mutual Information I(X;Y) vs. Source Probability P(X=1)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Source Probability q = P(X=1)")
    ax1.set_ylabel("Mutual Information (bits/symbol)")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend()

    # --- Plot 2: Mutual Information vs Crossover Probability p ---
    q_targets = [0.1, 0.2, 0.3, 0.5]
    for q, col in zip(q_targets, colors[:4]):
        mi = [bsc_mutual_information(q, p) for p in p_vals]
        label = f"q = {q:.1f} (symmetric)" if q == 0.5 else f"q = {q:.1f}"
        ax2.plot(p_vals, mi, label=label, color=col, linewidth=2)

    # Highlight Shannon Capacity of BSC (occurs at q=0.5)
    capacity = 1.0 - binary_entropy(p_vals)
    ax2.plot(p_vals, capacity, "k--", label="BSC Channel Capacity C = 1 - H(p)", linewidth=1.5)

    ax2.set_title("Mutual Information I(X;Y) vs. Channel Crossover Probability (p)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Crossover Probability p")
    ax2.set_ylabel("Mutual Information (bits/symbol)")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.legend()

    plt.suptitle("Information Theory: Mutual Information & Binary Symmetric Channel Capacity", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Print interesting details
    print("=== BSC Channel Capacity Summary ===")
    for p in [0.0, 0.01, 0.05, 0.1, 0.5]:
        cap = 1.0 - binary_entropy(p)
        print(f"  Crossover Probability (p) = {p:<5} | Capacity (C) = {cap:.4f} bits/symbol")


if __name__ == "__main__":
    main()
