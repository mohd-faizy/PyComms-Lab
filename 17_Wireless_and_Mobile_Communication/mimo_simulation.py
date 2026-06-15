import numpy as np


def main():
    rng = np.random.default_rng(31)
    n_tx = 2
    n_rx = 2
    snr_db = 20
    symbols = np.array([1 + 1j, -1 + 1j]) / np.sqrt(2)
    channel = (rng.normal(size=(n_rx, n_tx)) + 1j * rng.normal(size=(n_rx, n_tx))) / np.sqrt(2)
    noise_std = np.sqrt(1 / (2 * 10 ** (snr_db / 10)))
    noise = noise_std * (rng.normal(size=n_rx) + 1j * rng.normal(size=n_rx))
    received = channel @ symbols + noise
    estimated = np.linalg.pinv(channel) @ received
    singular_values = np.linalg.svd(channel, compute_uv=False)
    capacity = np.sum(np.log2(1 + (10 ** (snr_db / 10) / n_tx) * singular_values**2))

    print("Channel matrix:")
    print(np.round(channel, 3))
    print("Transmitted symbols:", np.round(symbols, 3))
    print("Zero-forcing estimate:", np.round(estimated, 3))
    print(f"2x2 MIMO capacity estimate: {capacity:.2f} bits/s/Hz")


if __name__ == "__main__":
    main()
