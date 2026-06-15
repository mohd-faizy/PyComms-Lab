# Advanced Modulation Visualizations

This folder contains deeper simulations for digital modulation topics that need
more than a basic constellation plot.

## Scripts

- `qam16_noise_dashboard.py` - text-to-16-QAM link with noisy channel,
  equalization, similarity scoring, and a six-panel dashboard.
- `qpsk_ber_constellation_dashboard.py` - QPSK constellation behavior and BER
  comparison over Eb/N0.
- `qam_order_comparison.py` - compares 4-QAM, 16-QAM, and 64-QAM symbol spacing
  and noise sensitivity.

The scripts display plots and try to save generated dashboard images under
`outputs/`. If a restricted environment blocks file writes, the simulation still
runs and reports the save error in the terminal.
