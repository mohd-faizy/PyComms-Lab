import numpy as np
import matplotlib.pyplot as plt


def add_awgn(signal_values, snr_db, rng):
    signal_power = np.mean(signal_values**2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    noise = rng.normal(scale=np.sqrt(noise_power), size=signal_values.size)
    return signal_values + noise, noise


def main():
    rng = np.random.default_rng(10)
    fs = 1000
    t = np.arange(0, 1, 1 / fs)
    clean = np.sin(2 * np.pi * 20 * t)
    noisy, noise = add_awgn(clean, snr_db=10, rng=rng)
    measured_snr = 10 * np.log10(np.mean(clean**2) / np.mean(noise**2))

    print(f"Measured SNR: {measured_snr:.2f} dB")

    plt.figure(figsize=(10, 4))
    plt.plot(t[:250], clean[:250], label="Clean")
    plt.plot(t[:250], noisy[:250], label="Noisy", alpha=0.8)
    plt.title("AWGN Channel")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
