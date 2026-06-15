# ECE Communication Engineering Simulations

![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Educational](https://img.shields.io/badge/Purpose-Educational-orange.svg)

A comprehensive, curriculum-aligned collection of Python-based simulations for core topics in Electronics and Communication Engineering (ECE). Designed for academic learning, lab assignments, and concept visualization.

## Tech Stack & Dependencies

- Python 3.x
- NumPy
- SciPy
- Matplotlib

Install the required packages using:
```bash
pip install -r requirements.txt
```

---

## Folder Guide (Systematic Curriculum Order)

This repository is structured sequentially to follow a standard Communication Engineering syllabus, from foundational probability and signals to digital transmission, wireless channels, network protocols, and emerging 5G/Radar technologies.

| # | Folder | Focus & Included Simulations |
|---|---|---|
| **01** | `01_Probability_Random_Variables_and_Noise` | Gaussian PDF/CDF, random processes (autocorrelation, PSD), noise types, Central Limit Theorem (CLT), probability distributions |
| **02** | `02_Signals_and_Systems` | Basic signal generation, convolution, Fourier series, FFT analysis, sampling & aliasing |
| **03** | `03_Analog_Modulation` | AM, FM, PM, SSB/DSB modulation & demodulation |
| **04** | `04_Digital_Modulation` | ASK, FSK, PSK (BPSK/QPSK), QAM, constellations, QPSK/QAM text transmission over noisy channel |
| **05** | `05_Pulse_Modulation` | PAM, PWM/PPM, PCM encoding/decoding, delta modulation, adaptive delta modulation |
| **06** | `06_Information_Theory_and_Coding` | Entropy, Shannon-Fano, Huffman coding, channel capacity, mutual information, rate-distortion, Lempel-Ziv (LZ78) coding |
| **07** | `07_Error_Control_Coding` | Linear block codes, Hamming codes, CRC, convolutional coding, Viterbi decoding, Reed-Solomon (15,11) coding, BCH codes, Turbo coding |
| **08** | `08_Data_Transmission_and_Line_Coding` | Line codes (NRZ, Manchester, AMI, B8ZS), eye diagram, ISI, raised cosine pulse shaping, baseband transmission, scrambler/descrambler |
| **09** | `09_AWGN_and_Channel_Modeling` | AWGN channels, Rayleigh & Rician fading, BER vs. SNR analysis, Shannon capacity limits, multipath delay spread, LS vs. MMSE channel estimation |
| **10** | `10_Multiplexing_and_Multiple_Access` | TDM, FDM, CDMA, OFDM, Wavelength Division Multiplexing (WDM), Pure & Slotted ALOHA |
| **11** | `11_Transmitter_and_Receiver_Design` | Superheterodyne receiver, Phase-Locked Loop (PLL), Automatic Gain Control (AGC), direct conversion receiver, transmitter architecture |
| **12** | `12_Spread_Spectrum_Communication` | DSSS, FHSS, PN sequence generation (LFSR), processing gain |
| **13** | `13_DSP_for_Communication` | Correlation receiver, FIR/IIR digital filters, equalization, matched filtering |
| **14** | `14_Antenna_and_Wave_Propagation` | Radiation patterns, Friis transmission equation, ground wave propagation, link budget calculator |
| **15** | `15_Optical_Communication` | Fiber attenuation, numerical aperture, optical BER, chromatic dispersion analysis, optical link budget |
| **16** | `16_Satellite_Communication` | Orbital parameters, Doppler shift, satellite link budget |
| **17** | `17_Wireless_and_Mobile_Communication` | Cellular frequency reuse, handoff, MIMO capacity, path loss models, OFDM wireless, receiver diversity combining (SC, EGC, MRC) |
| **18** | `18_Network_Protocols_and_Data_Link` | ARQ protocols (Stop-and-Wait, Go-Back-N, Selective Repeat), sliding window flow control, frame-level error detection |
| **19** | `19_Radar_Communication` | Radar range equation, chirp pulse compression, Doppler radar velocity estimation |
| **20** | `20_Emerging_Technologies` | 5G NR numerology & slot structure, mmWave propagation with atmospheric loss, Massive MIMO beamforming, Cognitive Radio spectrum sensing |
| **21** | `21_Mini_Projects` | Socket chat app, SDR basics, spectrum analyzer GUI, speech signal compression |
| **22** | `22_Advanced_Modulation_Visualizations` | 16-QAM noise dashboard, QAM order comparison, QPSK BER dashboard |

---

## Simulation Scripts & Outputs

Below is the complete curriculum index of all simulation scripts, including direct links to their source code, saved console logs, and visual plots.

### 01. Probability Random Variables and Noise

Folder path: [`01_Probability_Random_Variables_and_Noise`](01_Probability_Random_Variables_and_Noise)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`central_limit_theorem.py`](01_Probability_Random_Variables_and_Noise/central_limit_theorem.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig1.png" width="300" alt="Plot 1"> <br> <img src="01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig2.png" width="300" alt="Plot 2"> |
| [`gaussian_pdf_cdf.py`](01_Probability_Random_Variables_and_Noise/gaussian_pdf_cdf.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/gaussian_pdf_cdf.png" width="300" alt="Plot"> |
| [`noise_types.py`](01_Probability_Random_Variables_and_Noise/noise_types.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/noise_types.png" width="300" alt="Plot"> |
| [`probability_distributions.py`](01_Probability_Random_Variables_and_Noise/probability_distributions.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/probability_distributions.png" width="300" alt="Plot"> |
| [`random_processes.py`](01_Probability_Random_Variables_and_Noise/random_processes.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/random_processes.png" width="300" alt="Plot"> |

### 02. Signals and Systems

Folder path: [`02_Signals_and_Systems`](02_Signals_and_Systems)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`basic_signals_generation.py`](02_Signals_and_Systems/basic_signals_generation.py) | <img src="02_Signals_and_Systems/outputs/basic_signals_generation.png" width="300" alt="Plot"> |
| [`convolution.py`](02_Signals_and_Systems/convolution.py) | <img src="02_Signals_and_Systems/outputs/convolution.png" width="300" alt="Plot"> |
| [`fft_analysis.py`](02_Signals_and_Systems/fft_analysis.py) | <img src="02_Signals_and_Systems/outputs/fft_analysis.png" width="300" alt="Plot"> |
| [`fourier_series.py`](02_Signals_and_Systems/fourier_series.py) | <img src="02_Signals_and_Systems/outputs/fourier_series.png" width="300" alt="Plot"> |
| [`sampling_aliasing.py`](02_Signals_and_Systems/sampling_aliasing.py) | <img src="02_Signals_and_Systems/outputs/sampling_aliasing.png" width="300" alt="Plot"> |

### 03. Analog Modulation

Folder path: [`03_Analog_Modulation`](03_Analog_Modulation)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`am_modulation_demodulation.py`](03_Analog_Modulation/am_modulation_demodulation.py) | <img src="03_Analog_Modulation/outputs/am_modulation_demodulation.png" width="300" alt="Plot"> |
| [`fm_modulation.py`](03_Analog_Modulation/fm_modulation.py) | <img src="03_Analog_Modulation/outputs/fm_modulation.png" width="300" alt="Plot"> |
| [`pm_modulation.py`](03_Analog_Modulation/pm_modulation.py) | <img src="03_Analog_Modulation/outputs/pm_modulation.png" width="300" alt="Plot"> |
| [`ssb_dsb_modulation.py`](03_Analog_Modulation/ssb_dsb_modulation.py) | <img src="03_Analog_Modulation/outputs/ssb_dsb_modulation.png" width="300" alt="Plot"> |

### 04. Digital Modulation

Folder path: [`04_Digital_Modulation`](04_Digital_Modulation)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`ask_modulation.py`](04_Digital_Modulation/ask_modulation.py) | <img src="04_Digital_Modulation/outputs/ask_modulation.png" width="300" alt="Plot"> |
| [`constellation_diagrams.py`](04_Digital_Modulation/constellation_diagrams.py) | <img src="04_Digital_Modulation/outputs/constellation_diagrams.png" width="300" alt="Plot"> |
| [`fsk_modulation.py`](04_Digital_Modulation/fsk_modulation.py) | <img src="04_Digital_Modulation/outputs/fsk_modulation.png" width="300" alt="Plot"> |
| [`psk_bpsk_qpsk.py`](04_Digital_Modulation/psk_bpsk_qpsk.py) | <img src="04_Digital_Modulation/outputs/psk_bpsk_qpsk.png" width="300" alt="Plot"> |
| [`qam16_modulation_demodulation.py`](04_Digital_Modulation/qam16_modulation_demodulation.py) | <img src="04_Digital_Modulation/outputs/qam16_modulation_demodulation.png" width="300" alt="Plot"> |
| [`qam_modulation.py`](04_Digital_Modulation/qam_modulation.py) | <img src="04_Digital_Modulation/outputs/qam_modulation.png" width="300" alt="Plot"> |
| [`qpsk_modulation_demodulation.py`](04_Digital_Modulation/qpsk_modulation_demodulation.py) | <img src="04_Digital_Modulation/outputs/qpsk_modulation_demodulation.png" width="300" alt="Plot"> |

### 05. Pulse Modulation

Folder path: [`05_Pulse_Modulation`](05_Pulse_Modulation)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`adaptive_delta_modulation.py`](05_Pulse_Modulation/adaptive_delta_modulation.py) | <img src="05_Pulse_Modulation/outputs/adaptive_delta_modulation.png" width="300" alt="Plot"> |
| [`delta_modulation.py`](05_Pulse_Modulation/delta_modulation.py) | <img src="05_Pulse_Modulation/outputs/delta_modulation.png" width="300" alt="Plot"> |
| [`pam.py`](05_Pulse_Modulation/pam.py) | <img src="05_Pulse_Modulation/outputs/pam.png" width="300" alt="Plot"> |
| [`pcm_encoding_decoding.py`](05_Pulse_Modulation/pcm_encoding_decoding.py) | <img src="05_Pulse_Modulation/outputs/pcm_encoding_decoding.png" width="300" alt="Plot"> |
| [`pwm_ppm.py`](05_Pulse_Modulation/pwm_ppm.py) | <img src="05_Pulse_Modulation/outputs/pwm_ppm.png" width="300" alt="Plot"> |

### 06. Information Theory and Coding

Folder path: [`06_Information_Theory_and_Coding`](06_Information_Theory_and_Coding)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`channel_capacity.py`](06_Information_Theory_and_Coding/channel_capacity.py) | <img src="06_Information_Theory_and_Coding/outputs/channel_capacity.png" width="300" alt="Plot"> |
| [`entropy_calculation.py`](06_Information_Theory_and_Coding/entropy_calculation.py) | - |
| [`huffman_coding.py`](06_Information_Theory_and_Coding/huffman_coding.py) | - |
| [`lempel_ziv_coding.py`](06_Information_Theory_and_Coding/lempel_ziv_coding.py) | <img src="06_Information_Theory_and_Coding/outputs/lempel_ziv_coding.png" width="300" alt="Plot"> |
| [`mutual_information.py`](06_Information_Theory_and_Coding/mutual_information.py) | <img src="06_Information_Theory_and_Coding/outputs/mutual_information.png" width="300" alt="Plot"> |
| [`rate_distortion.py`](06_Information_Theory_and_Coding/rate_distortion.py) | <img src="06_Information_Theory_and_Coding/outputs/rate_distortion.png" width="300" alt="Plot"> |
| [`shannon_fano_coding.py`](06_Information_Theory_and_Coding/shannon_fano_coding.py) | - |
| [`source_coding_efficiency.py`](06_Information_Theory_and_Coding/source_coding_efficiency.py) | - |

### 07. Error Control Coding

Folder path: [`07_Error_Control_Coding`](07_Error_Control_Coding)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`bch_code.py`](07_Error_Control_Coding/bch_code.py) | <img src="07_Error_Control_Coding/outputs/bch_code.png" width="300" alt="Plot"> |
| [`convolutional_coding.py`](07_Error_Control_Coding/convolutional_coding.py) | - |
| [`cyclic_redundancy_check.py`](07_Error_Control_Coding/cyclic_redundancy_check.py) | - |
| [`hamming_code.py`](07_Error_Control_Coding/hamming_code.py) | - |
| [`linear_block_codes.py`](07_Error_Control_Coding/linear_block_codes.py) | - |
| [`reed_solomon_coding.py`](07_Error_Control_Coding/reed_solomon_coding.py) | <img src="07_Error_Control_Coding/outputs/reed_solomon_coding.png" width="300" alt="Plot"> |
| [`turbo_code_basics.py`](07_Error_Control_Coding/turbo_code_basics.py) | <img src="07_Error_Control_Coding/outputs/turbo_code_basics.png" width="300" alt="Plot"> |
| [`viterbi_decoder.py`](07_Error_Control_Coding/viterbi_decoder.py) | - |

### 08. Data Transmission and Line Coding

Folder path: [`08_Data_Transmission_and_Line_Coding`](08_Data_Transmission_and_Line_Coding)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`baseband_transmission.py`](08_Data_Transmission_and_Line_Coding/baseband_transmission.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/baseband_transmission.png" width="300" alt="Plot"> |
| [`eye_diagram.py`](08_Data_Transmission_and_Line_Coding/eye_diagram.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/eye_diagram.png" width="300" alt="Plot"> |
| [`intersymbol_interference.py`](08_Data_Transmission_and_Line_Coding/intersymbol_interference.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig1.png" width="300" alt="Plot 1"> <br> <img src="08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig2.png" width="300" alt="Plot 2"> |
| [`line_coding_schemes.py`](08_Data_Transmission_and_Line_Coding/line_coding_schemes.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/line_coding_schemes.png" width="300" alt="Plot"> |
| [`scrambler_descrambler.py`](08_Data_Transmission_and_Line_Coding/scrambler_descrambler.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/scrambler_descrambler.png" width="300" alt="Plot"> |

### 09. AWGN and Channel Modeling

Folder path: [`09_AWGN_and_Channel_Modeling`](09_AWGN_and_Channel_Modeling)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`awgn_capacity.py`](09_AWGN_and_Channel_Modeling/awgn_capacity.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/awgn_capacity.png" width="300" alt="Plot"> |
| [`awgn_channel.py`](09_AWGN_and_Channel_Modeling/awgn_channel.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/awgn_channel.png" width="300" alt="Plot"> |
| [`ber_vs_snr_bpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_bpsk.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_bpsk.png" width="300" alt="Plot"> |
| [`ber_vs_snr_qpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_qpsk.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_qpsk.png" width="300" alt="Plot"> |
| [`channel_estimation.py`](09_AWGN_and_Channel_Modeling/channel_estimation.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/channel_estimation.png" width="300" alt="Plot"> |
| [`multipath_channel.py`](09_AWGN_and_Channel_Modeling/multipath_channel.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/multipath_channel.png" width="300" alt="Plot"> |
| [`rayleigh_fading.py`](09_AWGN_and_Channel_Modeling/rayleigh_fading.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/rayleigh_fading.png" width="300" alt="Plot"> |
| [`rician_fading.py`](09_AWGN_and_Channel_Modeling/rician_fading.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/rician_fading.png" width="300" alt="Plot"> |

### 10. Multiplexing and Multiple Access

Folder path: [`10_Multiplexing_and_Multiple_Access`](10_Multiplexing_and_Multiple_Access)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`aloha_simulation.py`](10_Multiplexing_and_Multiple_Access/aloha_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/aloha_simulation.png" width="300" alt="Plot"> |
| [`cdma_simulation.py`](10_Multiplexing_and_Multiple_Access/cdma_simulation.py) | - |
| [`fdm_simulation.py`](10_Multiplexing_and_Multiple_Access/fdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/fdm_simulation.png" width="300" alt="Plot"> |
| [`ofdm_simulation.py`](10_Multiplexing_and_Multiple_Access/ofdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/ofdm_simulation.png" width="300" alt="Plot"> |
| [`tdm_simulation.py`](10_Multiplexing_and_Multiple_Access/tdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/tdm_simulation.png" width="300" alt="Plot"> |
| [`wdm_simulation.py`](10_Multiplexing_and_Multiple_Access/wdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/wdm_simulation.png" width="300" alt="Plot"> |

### 11. Transmitter and Receiver Design

Folder path: [`11_Transmitter_and_Receiver_Design`](11_Transmitter_and_Receiver_Design)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`agc_automatic_gain_control.py`](11_Transmitter_and_Receiver_Design/agc_automatic_gain_control.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/agc_automatic_gain_control.png" width="300" alt="Plot"> |
| [`direct_conversion_receiver.py`](11_Transmitter_and_Receiver_Design/direct_conversion_receiver.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/direct_conversion_receiver.png" width="300" alt="Plot"> |
| [`pll_phase_locked_loop.py`](11_Transmitter_and_Receiver_Design/pll_phase_locked_loop.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/pll_phase_locked_loop.png" width="300" alt="Plot"> |
| [`superheterodyne_receiver.py`](11_Transmitter_and_Receiver_Design/superheterodyne_receiver.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/superheterodyne_receiver.png" width="300" alt="Plot"> |
| [`transmitter_architecture.py`](11_Transmitter_and_Receiver_Design/transmitter_architecture.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/transmitter_architecture.png" width="300" alt="Plot"> |

### 12. Spread Spectrum Communication

Folder path: [`12_Spread_Spectrum_Communication`](12_Spread_Spectrum_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`dsss_direct_sequence.py`](12_Spread_Spectrum_Communication/dsss_direct_sequence.py) | <img src="12_Spread_Spectrum_Communication/outputs/dsss_direct_sequence.png" width="300" alt="Plot"> |
| [`fhss_frequency_hopping.py`](12_Spread_Spectrum_Communication/fhss_frequency_hopping.py) | <img src="12_Spread_Spectrum_Communication/outputs/fhss_frequency_hopping.png" width="300" alt="Plot"> |
| [`pn_sequence_generator.py`](12_Spread_Spectrum_Communication/pn_sequence_generator.py) | <img src="12_Spread_Spectrum_Communication/outputs/pn_sequence_generator.png" width="300" alt="Plot"> |
| [`processing_gain.py`](12_Spread_Spectrum_Communication/processing_gain.py) | <img src="12_Spread_Spectrum_Communication/outputs/processing_gain.png" width="300" alt="Plot"> |

### 13. DSP for Communication

Folder path: [`13_DSP_for_Communication`](13_DSP_for_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`correlation_receiver.py`](13_DSP_for_Communication/correlation_receiver.py) | <img src="13_DSP_for_Communication/outputs/correlation_receiver.png" width="300" alt="Plot"> |
| [`digital_filters_fir_iir.py`](13_DSP_for_Communication/digital_filters_fir_iir.py) | <img src="13_DSP_for_Communication/outputs/digital_filters_fir_iir.png" width="300" alt="Plot"> |
| [`equalization.py`](13_DSP_for_Communication/equalization.py) | <img src="13_DSP_for_Communication/outputs/equalization.png" width="300" alt="Plot"> |
| [`matched_filter.py`](13_DSP_for_Communication/matched_filter.py) | <img src="13_DSP_for_Communication/outputs/matched_filter.png" width="300" alt="Plot"> |

### 14. Antenna and Wave Propagation

Folder path: [`14_Antenna_and_Wave_Propagation`](14_Antenna_and_Wave_Propagation)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`friis_transmission_equation.py`](14_Antenna_and_Wave_Propagation/friis_transmission_equation.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/friis_transmission_equation.png" width="300" alt="Plot"> |
| [`ground_wave_propagation.py`](14_Antenna_and_Wave_Propagation/ground_wave_propagation.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/ground_wave_propagation.png" width="300" alt="Plot"> |
| [`link_budget_calculator.py`](14_Antenna_and_Wave_Propagation/link_budget_calculator.py) | - |
| [`radiation_pattern.py`](14_Antenna_and_Wave_Propagation/radiation_pattern.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/radiation_pattern.png" width="300" alt="Plot"> |

### 15. Optical Communication

Folder path: [`15_Optical_Communication`](15_Optical_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`ber_optical_link.py`](15_Optical_Communication/ber_optical_link.py) | <img src="15_Optical_Communication/outputs/ber_optical_link.png" width="300" alt="Plot"> |
| [`dispersion_analysis.py`](15_Optical_Communication/dispersion_analysis.py) | <img src="15_Optical_Communication/outputs/dispersion_analysis.png" width="300" alt="Plot"> |
| [`fiber_attenuation.py`](15_Optical_Communication/fiber_attenuation.py) | <img src="15_Optical_Communication/outputs/fiber_attenuation.png" width="300" alt="Plot"> |
| [`numerical_aperture.py`](15_Optical_Communication/numerical_aperture.py) | - |
| [`optical_link_budget.py`](15_Optical_Communication/optical_link_budget.py) | <img src="15_Optical_Communication/outputs/optical_link_budget.png" width="300" alt="Plot"> |

### 16. Satellite Communication

Folder path: [`16_Satellite_Communication`](16_Satellite_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`doppler_shift_satellite.py`](16_Satellite_Communication/doppler_shift_satellite.py) | <img src="16_Satellite_Communication/outputs/doppler_shift_satellite.png" width="300" alt="Plot"> |
| [`link_budget_satellite.py`](16_Satellite_Communication/link_budget_satellite.py) | - |
| [`orbital_parameters.py`](16_Satellite_Communication/orbital_parameters.py) | - |

### 17. Wireless and Mobile Communication

Folder path: [`17_Wireless_and_Mobile_Communication`](17_Wireless_and_Mobile_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`cellular_frequency_reuse.py`](17_Wireless_and_Mobile_Communication/cellular_frequency_reuse.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/cellular_frequency_reuse.png" width="300" alt="Plot"> |
| [`diversity_techniques.py`](17_Wireless_and_Mobile_Communication/diversity_techniques.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/diversity_techniques.png" width="300" alt="Plot"> |
| [`handoff_simulation.py`](17_Wireless_and_Mobile_Communication/handoff_simulation.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/handoff_simulation.png" width="300" alt="Plot"> |
| [`mimo_simulation.py`](17_Wireless_and_Mobile_Communication/mimo_simulation.py) | - |
| [`ofdm_wireless.py`](17_Wireless_and_Mobile_Communication/ofdm_wireless.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/ofdm_wireless.png" width="300" alt="Plot"> |
| [`path_loss_models.py`](17_Wireless_and_Mobile_Communication/path_loss_models.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/path_loss_models.png" width="300" alt="Plot"> |

### 18. Network Protocols and Data Link

Folder path: [`18_Network_Protocols_and_Data_Link`](18_Network_Protocols_and_Data_Link)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`arq_protocols.py`](18_Network_Protocols_and_Data_Link/arq_protocols.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/arq_protocols.png" width="300" alt="Plot"> |
| [`error_detection_protocols.py`](18_Network_Protocols_and_Data_Link/error_detection_protocols.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/error_detection_protocols.png" width="300" alt="Plot"> |
| [`flow_control.py`](18_Network_Protocols_and_Data_Link/flow_control.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/flow_control.png" width="300" alt="Plot"> |

### 19. Radar Communication

Folder path: [`19_Radar_Communication`](19_Radar_Communication)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`doppler_radar.py`](19_Radar_Communication/doppler_radar.py) | <img src="19_Radar_Communication/outputs/doppler_radar.png" width="300" alt="Plot"> |
| [`pulse_compression.py`](19_Radar_Communication/pulse_compression.py) | <img src="19_Radar_Communication/outputs/pulse_compression.png" width="300" alt="Plot"> |
| [`radar_range_equation.py`](19_Radar_Communication/radar_range_equation.py) | <img src="19_Radar_Communication/outputs/radar_range_equation.png" width="300" alt="Plot"> |

### 20. Emerging Technologies

Folder path: [`20_Emerging_Technologies`](20_Emerging_Technologies)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`5g_nr_basics.py`](20_Emerging_Technologies/5g_nr_basics.py) | <img src="20_Emerging_Technologies/outputs/5g_nr_basics.png" width="300" alt="Plot"> |
| [`cognitive_radio.py`](20_Emerging_Technologies/cognitive_radio.py) | <img src="20_Emerging_Technologies/outputs/cognitive_radio.png" width="300" alt="Plot"> |
| [`massive_mimo.py`](20_Emerging_Technologies/massive_mimo.py) | <img src="20_Emerging_Technologies/outputs/massive_mimo.png" width="300" alt="Plot"> |
| [`mmwave_propagation.py`](20_Emerging_Technologies/mmwave_propagation.py) | <img src="20_Emerging_Technologies/outputs/mmwave_propagation.png" width="300" alt="Plot"> |

### 21. Mini Projects

Folder path: [`21_Mini_Projects`](21_Mini_Projects)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`chat_application_socket.py`](21_Mini_Projects/chat_application_socket.py) | - |
| [`digital_filter_designer.py`](21_Mini_Projects/digital_filter_designer.py) | <img src="21_Mini_Projects/outputs/digital_filter_designer.png" width="300" alt="Plot"> |
| [`dtmf_dialpad_simulator.py`](21_Mini_Projects/dtmf_dialpad_simulator.py) | <img src="21_Mini_Projects/outputs/dtmf_dialpad_simulator.png" width="300" alt="Plot"> |
| [`software_defined_radio_basics.py`](21_Mini_Projects/software_defined_radio_basics.py) | <img src="21_Mini_Projects/outputs/software_defined_radio_basics.png" width="300" alt="Plot"> |
| [`spectrum_analyzer_gui.py`](21_Mini_Projects/spectrum_analyzer_gui.py) | <img src="21_Mini_Projects/outputs/spectrum_analyzer_gui.png" width="300" alt="Plot"> |
| [`speech_signal_compression.py`](21_Mini_Projects/speech_signal_compression.py) | <img src="21_Mini_Projects/outputs/speech_signal_compression.png" width="300" alt="Plot"> |

### 22. Advanced Modulation Visualizations

Folder path: [`22_Advanced_Modulation_Visualizations`](22_Advanced_Modulation_Visualizations)

| Simulation Script | Output Plot(s) |
| :--- | :--- |
| [`qam16_noise_dashboard.py`](22_Advanced_Modulation_Visualizations/qam16_noise_dashboard.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qam16_noise_dashboard.png" width="300" alt="Plot"> |
| [`qam_order_comparison.py`](22_Advanced_Modulation_Visualizations/qam_order_comparison.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qam_order_comparison.png" width="300" alt="Plot"> |
| [`qpsk_ber_constellation_dashboard.py`](22_Advanced_Modulation_Visualizations/qpsk_ber_constellation_dashboard.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qpsk_ber_constellation_dashboard.png" width="300" alt="Plot"> |


## How to Run

Run any simulation from the repository root:
```bash
# General run command
python <folder_name>/<script_name>.py

# Example: Run 5G NR Numerology Simulation
python 20_Emerging_Technologies/5g_nr_basics.py

# Example: Run Massive MIMO Precoding & Beamforming
python 20_Emerging_Technologies/massive_mimo.py

# Example: Run Sliding Window Flow Control
python 18_Network_Protocols_and_Data_Link/flow_control.py
```

Most scripts display an interactive Matplotlib plot and print quantitative performance results to the console.

## Highlighted Advanced Examples

- **Massive MIMO Beamforming (`20_Emerging_Technologies/massive_mimo.py`)**: Models a Uniform Linear Array (ULA) at a Base Station and simulates Zero Forcing (ZF), Minimum Mean Squared Error (MMSE), and Maximum Ratio Transmission (MRT) precoders, plotting sum-rate scaling and beam radiation patterns.
- **Turbo Codes (`07_Error_Control_Coding/turbo_code_basics.py`)**: Simulates a parallel concatenated systematic convolutional code with iterative soft-decision feedback decoding, showing how BER improves iteration by iteration.
- **OFDM Wireless System (`17_Wireless_and_Mobile_Communication/ofdm_wireless.py`)**: Contains a full transceiver chain: IFFT modulation, Cyclic Prefix (CP) insertion, multipath channel convolution, FFT demodulation, and 1-tap frequency domain equalization (FEQ).

## License

MIT
