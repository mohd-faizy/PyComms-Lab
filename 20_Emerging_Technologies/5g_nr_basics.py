"""5G NR (New Radio) Numerology and Slot Structure.

Visualises 5G NR flexible numerology (subcarrier spacing and symbol duration)
and the resulting slot structure in the time domain.
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_numerology_params(mu):
    """Calculate subcarrier spacing and symbol duration for given numerology index mu.

    SCS = 15 * 2^mu kHz
    Slot duration = 1 ms / 2^mu
    Number of OFDM symbols per slot = 14 (normal CP)
    """
    scs = 15 * (2**mu)  # in kHz
    slot_duration = 1.0 / (2**mu)  # in ms
    symbol_duration_us = (1.0 / (scs * 1e3)) * 1e6  # in microseconds (approx, excluding CP)
    slots_per_subframe = 2**mu
    slots_per_frame = 10 * slots_per_subframe
    return scs, slot_duration, symbol_duration_us, slots_per_subframe, slots_per_frame


def main():
    mus = [0, 1, 2, 3, 4]
    use_cases = [
        "LTE / 5G NR (FR1: <6 GHz, eMBB)",
        "5G NR (FR1: <6 GHz, eMBB/URLLC)",
        "5G NR (FR1: <6 GHz or FR2: mmWave)",
        "5G NR (FR2: mmWave, high throughput)",
        "5G NR (FR2: mmWave, ultra-wide band)"
    ]

    print("=== 5G NR Numerologies (Flexible Subcarrier Spacing) ===")
    print(f"{'mu':<3} | {'SCS (kHz)':<10} | {'Slot Dur (ms)':<15} | {'Sym Dur (us)':<15} | {'Slots/Subframe':<15} | {'Primary Use Case'}")
    print("-" * 95)
    for mu, use_case in zip(mus, use_cases):
        scs, slot_dur, sym_dur, s_sf, s_f = calculate_numerology_params(mu)
        print(f"{mu:<3} | {scs:<10} | {slot_dur:<15.4f} | {sym_dur:<15.2f} | {s_sf:<15} | {use_case}")

    # --- Plotting Subcarrier Spacing (Frequency Domain) ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    colors = ["r", "c", "gray", "gray", "orange"]
    
    # We will draw a few adjacent subcarriers for different numerologies
    for idx, mu in enumerate([0, 1, 2, 3]):
        scs = 15 * (2**mu)
        # Center frequency offset for display
        center_freqs = np.arange(-3, 4) * scs
        for fc in center_freqs:
            # draw a sinc-like carrier shape
            f = np.linspace(fc - scs, fc + scs, 100)
            sinc_val = np.sinc((f - fc) / scs) ** 2
            ax1.plot(f, sinc_val, color=colors[idx], alpha=0.7, 
                     label=f"mu={mu} ({scs} kHz SCS)" if fc == center_freqs[0] else "")

    ax1.set_title("5G NR Subcarrier Spacing (Frequency Domain Comparison)", fontsize=12)
    ax1.set_xlabel("Frequency Offset (kHz)")
    ax1.set_ylabel("Normalized Power Spectral Density")
    ax1.set_xlim(-150, 150)
    ax1.grid(True, alpha=0.3)
    # Get unique labels
    handles, labels = ax1.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax1.legend(by_label.values(), by_label.keys(), loc="upper right")

    # --- Plotting Slot Structure (Time Domain) ---
    # We will draw a 1 ms subframe and show how it is partitioned into slots
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(-0.5, 4.5)
    
    for mu in [0, 1, 2, 3]:
        slots_in_sf = 2**mu
        slot_w = 1.0 / slots_in_sf
        for s in range(slots_in_sf):
            # Plot rectangle for slot
            rect = plt.Rectangle((s * slot_w, mu - 0.3), slot_w, 0.6,
                                 facecolor=colors[mu], edgecolor="black", alpha=0.6)
            ax2.add_patch(rect)
            # Label slot index if it fits
            if slots_in_sf <= 8:
                ax2.text(s * slot_w + slot_w/2, mu, f"Slot {s}", 
                         ha="center", va="center", color="black", fontsize=9, fontweight="bold")
            elif s % (slots_in_sf // 4) == 0:
                ax2.text(s * slot_w + slot_w/2, mu, f"S{s}", 
                         ha="center", va="center", color="black", fontsize=8)

    ax2.set_yticks([0, 1, 2, 3])
    ax2.set_yticklabels([
        "mu=0 (15 kHz, 1 slot/ms)",
        "mu=1 (30 kHz, 2 slots/ms)",
        "mu=2 (60 kHz, 4 slots/ms)",
        "mu=3 (120 kHz, 8 slots/ms)"
    ])
    ax2.set_title("5G NR Time-Domain Slot Structure (in a 1 ms Subframe)", fontsize=12)
    ax2.set_xlabel("Time (ms)")
    ax2.grid(True, axis="x", alpha=0.5)

    plt.suptitle("5G NR Flexible Numerology (SCS and Frame Structure)", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
