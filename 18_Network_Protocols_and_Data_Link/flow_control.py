"""Sliding window flow control simulation.

Simulates the sliding window protocol and analyses throughput as a
function of window size, propagation delay, and frame error rate.
"""

import numpy as np
import matplotlib.pyplot as plt


def sliding_window_throughput(window_size, prop_delay, frame_time, per, n_frames,
                               rng):
    """Estimate throughput of a sliding-window protocol.

    Parameters
    ----------
    window_size : int   - Maximum outstanding (unacked) frames
    prop_delay : float  - One-way propagation delay (seconds)
    frame_time : float  - Time to transmit one frame (seconds)
    per : float         - Frame error rate
    n_frames : int      - Total frames to deliver
    """
    rtt = 2 * prop_delay + frame_time
    a = prop_delay / frame_time  # bandwidth-delay product

    # Ideal utilisation (no errors)
    if window_size >= (1 + 2 * a):
        utilisation = 1.0
    else:
        utilisation = window_size / (1 + 2 * a)

    # Account for errors (selective repeat model)
    effective = utilisation * (1 - per)
    total_time = n_frames * frame_time / effective if effective > 0 else np.inf
    throughput = n_frames / total_time * frame_time  # normalised
    return throughput, utilisation


def main():
    frame_time = 0.001  # 1 ms
    prop_delay = 0.010  # 10 ms
    n_frames = 1000
    rng = np.random.default_rng(42)

    # --- Window size analysis ---
    window_sizes = np.arange(1, 65)
    per_values = [0.0, 0.05, 0.10, 0.20]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for per in per_values:
        thputs = []
        for ws in window_sizes:
            tp, _ = sliding_window_throughput(ws, prop_delay, frame_time,
                                              per, n_frames, rng)
            thputs.append(tp)
        axes[0].plot(window_sizes, thputs, label=f"FER = {per*100:.0f}%")

    axes[0].axvline(x=1 + 2 * prop_delay / frame_time, ls="--", color="grey",
                    lw=1, label="W = 1+2a")
    axes[0].set_title("Throughput vs Window Size")
    axes[0].set_xlabel("Window Size (frames)")
    axes[0].set_ylabel("Normalised Throughput")
    axes[0].legend()
    axes[0].grid(True)

    # --- Delay analysis ---
    delays = np.linspace(0.001, 0.050, 50)
    ws_vals = [1, 4, 8, 21, 40]

    for ws in ws_vals:
        thputs = []
        for d in delays:
            tp, _ = sliding_window_throughput(ws, d, frame_time, 0.0,
                                              n_frames, rng)
            thputs.append(tp)
        axes[1].plot(delays * 1000, thputs, label=f"W = {ws}")

    axes[1].set_title("Throughput vs Propagation Delay")
    axes[1].set_xlabel("Propagation Delay (ms)")
    axes[1].set_ylabel("Normalised Throughput")
    axes[1].legend()
    axes[1].grid(True)

    fig.suptitle("Sliding Window Flow Control", fontsize=13)
    fig.tight_layout()
    plt.show()

    a = prop_delay / frame_time
    print(f"Frame time: {frame_time*1000:.1f} ms")
    print(f"Propagation delay: {prop_delay*1000:.1f} ms")
    print(f"Bandwidth-delay product (a): {a:.1f}")
    print(f"Minimum window for full utilisation: {int(1 + 2*a)}")


if __name__ == "__main__":
    main()
