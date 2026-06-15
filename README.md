# ECE Communication Engineering Simulations

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

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`central_limit_theorem.py`](01_Probability_Random_Variables_and_Noise/central_limit_theorem.py) | [Log](01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem.txt) | [Plot 1](01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig1.png), [Plot 2](01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig2.png) | Central Limit Theorem demonstration. |
| [`gaussian_pdf_cdf.py`](01_Probability_Random_Variables_and_Noise/gaussian_pdf_cdf.py) | [Log](01_Probability_Random_Variables_and_Noise/outputs/gaussian_pdf_cdf.txt) | [Plot](01_Probability_Random_Variables_and_Noise/outputs/gaussian_pdf_cdf.png) | Gaussian PDF and CDF visualization. |
| [`noise_types.py`](01_Probability_Random_Variables_and_Noise/noise_types.py) | [Log](01_Probability_Random_Variables_and_Noise/outputs/noise_types.txt) | [Plot](01_Probability_Random_Variables_and_Noise/outputs/noise_types.png) | Noise types in communication systems. |
| [`probability_distributions.py`](01_Probability_Random_Variables_and_Noise/probability_distributions.py) | [Log](01_Probability_Random_Variables_and_Noise/outputs/probability_distributions.txt) | [Plot](01_Probability_Random_Variables_and_Noise/outputs/probability_distributions.png) | Probability distributions used in communication engineering. |
| [`random_processes.py`](01_Probability_Random_Variables_and_Noise/random_processes.py) | [Log](01_Probability_Random_Variables_and_Noise/outputs/random_processes.txt) | [Plot](01_Probability_Random_Variables_and_Noise/outputs/random_processes.png) | Random processes: autocorrelation and power spectral density. |

### 02. Signals and Systems

Folder path: [`02_Signals_and_Systems`](02_Signals_and_Systems)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`basic_signals_generation.py`](02_Signals_and_Systems/basic_signals_generation.py) | [Log](02_Signals_and_Systems/outputs/basic_signals_generation.txt) | [Plot](02_Signals_and_Systems/outputs/basic_signals_generation.png) | Simulation script. |
| [`convolution.py`](02_Signals_and_Systems/convolution.py) | [Log](02_Signals_and_Systems/outputs/convolution.txt) | [Plot](02_Signals_and_Systems/outputs/convolution.png) | Simulation script. |
| [`fft_analysis.py`](02_Signals_and_Systems/fft_analysis.py) | [Log](02_Signals_and_Systems/outputs/fft_analysis.txt) | [Plot](02_Signals_and_Systems/outputs/fft_analysis.png) | Simulation script. |
| [`fourier_series.py`](02_Signals_and_Systems/fourier_series.py) | [Log](02_Signals_and_Systems/outputs/fourier_series.txt) | [Plot](02_Signals_and_Systems/outputs/fourier_series.png) | Simulation script. |
| [`sampling_aliasing.py`](02_Signals_and_Systems/sampling_aliasing.py) | [Log](02_Signals_and_Systems/outputs/sampling_aliasing.txt) | [Plot](02_Signals_and_Systems/outputs/sampling_aliasing.png) | Simulation script. |

### 03. Analog Modulation

Folder path: [`03_Analog_Modulation`](03_Analog_Modulation)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`am_modulation_demodulation.py`](03_Analog_Modulation/am_modulation_demodulation.py) | [Log](03_Analog_Modulation/outputs/am_modulation_demodulation.txt) | [Plot](03_Analog_Modulation/outputs/am_modulation_demodulation.png) | Simulation script. |
| [`fm_modulation.py`](03_Analog_Modulation/fm_modulation.py) | [Log](03_Analog_Modulation/outputs/fm_modulation.txt) | [Plot](03_Analog_Modulation/outputs/fm_modulation.png) | Simulation script. |
| [`pm_modulation.py`](03_Analog_Modulation/pm_modulation.py) | [Log](03_Analog_Modulation/outputs/pm_modulation.txt) | [Plot](03_Analog_Modulation/outputs/pm_modulation.png) | Simulation script. |
| [`ssb_dsb_modulation.py`](03_Analog_Modulation/ssb_dsb_modulation.py) | [Log](03_Analog_Modulation/outputs/ssb_dsb_modulation.txt) | [Plot](03_Analog_Modulation/outputs/ssb_dsb_modulation.png) | Simulation script. |

### 04. Digital Modulation

Folder path: [`04_Digital_Modulation`](04_Digital_Modulation)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`ask_modulation.py`](04_Digital_Modulation/ask_modulation.py) | [Log](04_Digital_Modulation/outputs/ask_modulation.txt) | [Plot](04_Digital_Modulation/outputs/ask_modulation.png) | Simulation script. |
| [`constellation_diagrams.py`](04_Digital_Modulation/constellation_diagrams.py) | [Log](04_Digital_Modulation/outputs/constellation_diagrams.txt) | [Plot](04_Digital_Modulation/outputs/constellation_diagrams.png) | Simulation script. |
| [`fsk_modulation.py`](04_Digital_Modulation/fsk_modulation.py) | [Log](04_Digital_Modulation/outputs/fsk_modulation.txt) | [Plot](04_Digital_Modulation/outputs/fsk_modulation.png) | Simulation script. |
| [`psk_bpsk_qpsk.py`](04_Digital_Modulation/psk_bpsk_qpsk.py) | [Log](04_Digital_Modulation/outputs/psk_bpsk_qpsk.txt) | [Plot](04_Digital_Modulation/outputs/psk_bpsk_qpsk.png) | Simulation script. |
| [`qam16_modulation_demodulation.py`](04_Digital_Modulation/qam16_modulation_demodulation.py) | [Log](04_Digital_Modulation/outputs/qam16_modulation_demodulation.txt) | [Plot](04_Digital_Modulation/outputs/qam16_modulation_demodulation.png) | Simulation script. |
| [`qam_modulation.py`](04_Digital_Modulation/qam_modulation.py) | [Log](04_Digital_Modulation/outputs/qam_modulation.txt) | [Plot](04_Digital_Modulation/outputs/qam_modulation.png) | Simulation script. |
| [`qpsk_modulation_demodulation.py`](04_Digital_Modulation/qpsk_modulation_demodulation.py) | [Log](04_Digital_Modulation/outputs/qpsk_modulation_demodulation.txt) | [Plot](04_Digital_Modulation/outputs/qpsk_modulation_demodulation.png) | Simulation script. |

### 05. Pulse Modulation

Folder path: [`05_Pulse_Modulation`](05_Pulse_Modulation)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`adaptive_delta_modulation.py`](05_Pulse_Modulation/adaptive_delta_modulation.py) | [Log](05_Pulse_Modulation/outputs/adaptive_delta_modulation.txt) | [Plot](05_Pulse_Modulation/outputs/adaptive_delta_modulation.png) | Simulation script. |
| [`delta_modulation.py`](05_Pulse_Modulation/delta_modulation.py) | [Log](05_Pulse_Modulation/outputs/delta_modulation.txt) | [Plot](05_Pulse_Modulation/outputs/delta_modulation.png) | Simulation script. |
| [`pam.py`](05_Pulse_Modulation/pam.py) | [Log](05_Pulse_Modulation/outputs/pam.txt) | [Plot](05_Pulse_Modulation/outputs/pam.png) | Simulation script. |
| [`pcm_encoding_decoding.py`](05_Pulse_Modulation/pcm_encoding_decoding.py) | [Log](05_Pulse_Modulation/outputs/pcm_encoding_decoding.txt) | [Plot](05_Pulse_Modulation/outputs/pcm_encoding_decoding.png) | Simulation script. |
| [`pwm_ppm.py`](05_Pulse_Modulation/pwm_ppm.py) | [Log](05_Pulse_Modulation/outputs/pwm_ppm.txt) | [Plot](05_Pulse_Modulation/outputs/pwm_ppm.png) | Simulation script. |

### 06. Information Theory and Coding

Folder path: [`06_Information_Theory_and_Coding`](06_Information_Theory_and_Coding)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`channel_capacity.py`](06_Information_Theory_and_Coding/channel_capacity.py) | [Log](06_Information_Theory_and_Coding/outputs/channel_capacity.txt) | [Plot](06_Information_Theory_and_Coding/outputs/channel_capacity.png) | Simulation script. |
| [`entropy_calculation.py`](06_Information_Theory_and_Coding/entropy_calculation.py) | [Log](06_Information_Theory_and_Coding/outputs/entropy_calculation.txt) | - | Simulation script. |
| [`huffman_coding.py`](06_Information_Theory_and_Coding/huffman_coding.py) | [Log](06_Information_Theory_and_Coding/outputs/huffman_coding.txt) | - | Simulation script. |
| [`lempel_ziv_coding.py`](06_Information_Theory_and_Coding/lempel_ziv_coding.py) | [Log](06_Information_Theory_and_Coding/outputs/lempel_ziv_coding.txt) | [Plot](06_Information_Theory_and_Coding/outputs/lempel_ziv_coding.png) | Lempel-Ziv (LZ78) Compression Algorithm Demonstration. |
| [`mutual_information.py`](06_Information_Theory_and_Coding/mutual_information.py) | [Log](06_Information_Theory_and_Coding/outputs/mutual_information.txt) | [Plot](06_Information_Theory_and_Coding/outputs/mutual_information.png) | Mutual Information and BSC Channel Capacity. |
| [`rate_distortion.py`](06_Information_Theory_and_Coding/rate_distortion.py) | [Log](06_Information_Theory_and_Coding/outputs/rate_distortion.txt) | [Plot](06_Information_Theory_and_Coding/outputs/rate_distortion.png) | Rate-Distortion Functions for Gaussian and Binary Sources. |
| [`shannon_fano_coding.py`](06_Information_Theory_and_Coding/shannon_fano_coding.py) | [Log](06_Information_Theory_and_Coding/outputs/shannon_fano_coding.txt) | - | Simulation script. |
| [`source_coding_efficiency.py`](06_Information_Theory_and_Coding/source_coding_efficiency.py) | [Log](06_Information_Theory_and_Coding/outputs/source_coding_efficiency.txt) | - | Simulation script. |

### 07. Error Control Coding

Folder path: [`07_Error_Control_Coding`](07_Error_Control_Coding)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`bch_code.py`](07_Error_Control_Coding/bch_code.py) | [Log](07_Error_Control_Coding/outputs/bch_code.txt) | [Plot](07_Error_Control_Coding/outputs/bch_code.png) | Bose-Chaudhuri-Hocquenghem (BCH) Cyclic Code. |
| [`convolutional_coding.py`](07_Error_Control_Coding/convolutional_coding.py) | [Log](07_Error_Control_Coding/outputs/convolutional_coding.txt) | - | Simulation script. |
| [`cyclic_redundancy_check.py`](07_Error_Control_Coding/cyclic_redundancy_check.py) | [Log](07_Error_Control_Coding/outputs/cyclic_redundancy_check.txt) | - | Simulation script. |
| [`hamming_code.py`](07_Error_Control_Coding/hamming_code.py) | [Log](07_Error_Control_Coding/outputs/hamming_code.txt) | - | Simulation script. |
| [`linear_block_codes.py`](07_Error_Control_Coding/linear_block_codes.py) | [Log](07_Error_Control_Coding/outputs/linear_block_codes.txt) | - | Simulation script. |
| [`reed_solomon_coding.py`](07_Error_Control_Coding/reed_solomon_coding.py) | [Log](07_Error_Control_Coding/outputs/reed_solomon_coding.txt) | [Plot](07_Error_Control_Coding/outputs/reed_solomon_coding.png) | Reed-Solomon Error Control Coding. |
| [`turbo_code_basics.py`](07_Error_Control_Coding/turbo_code_basics.py) | [Log](07_Error_Control_Coding/outputs/turbo_code_basics.txt) | [Plot](07_Error_Control_Coding/outputs/turbo_code_basics.png) | Turbo Code Encoder and Iterative Decoder. |
| [`viterbi_decoder.py`](07_Error_Control_Coding/viterbi_decoder.py) | [Log](07_Error_Control_Coding/outputs/viterbi_decoder.txt) | - | Simulation script. |

### 08. Data Transmission and Line Coding

Folder path: [`08_Data_Transmission_and_Line_Coding`](08_Data_Transmission_and_Line_Coding)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`baseband_transmission.py`](08_Data_Transmission_and_Line_Coding/baseband_transmission.py) | [Log](08_Data_Transmission_and_Line_Coding/outputs/baseband_transmission.txt) | [Plot](08_Data_Transmission_and_Line_Coding/outputs/baseband_transmission.png) | Complete baseband digital transmission system. |
| [`eye_diagram.py`](08_Data_Transmission_and_Line_Coding/eye_diagram.py) | [Log](08_Data_Transmission_and_Line_Coding/outputs/eye_diagram.txt) | [Plot](08_Data_Transmission_and_Line_Coding/outputs/eye_diagram.png) | Eye diagram generation for baseband digital transmission. |
| [`intersymbol_interference.py`](08_Data_Transmission_and_Line_Coding/intersymbol_interference.py) | [Log](08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference.txt) | [Plot 1](08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig1.png), [Plot 2](08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig2.png) | Inter-Symbol Interference (ISI) and pulse shaping. |
| [`line_coding_schemes.py`](08_Data_Transmission_and_Line_Coding/line_coding_schemes.py) | [Log](08_Data_Transmission_and_Line_Coding/outputs/line_coding_schemes.txt) | [Plot](08_Data_Transmission_and_Line_Coding/outputs/line_coding_schemes.png) | Line coding schemes used in digital data transmission. |
| [`scrambler_descrambler.py`](08_Data_Transmission_and_Line_Coding/scrambler_descrambler.py) | [Log](08_Data_Transmission_and_Line_Coding/outputs/scrambler_descrambler.txt) | [Plot](08_Data_Transmission_and_Line_Coding/outputs/scrambler_descrambler.png) | Scrambler and descrambler for digital data transmission. |

### 09. AWGN and Channel Modeling

Folder path: [`09_AWGN_and_Channel_Modeling`](09_AWGN_and_Channel_Modeling)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`awgn_capacity.py`](09_AWGN_and_Channel_Modeling/awgn_capacity.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/awgn_capacity.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/awgn_capacity.png) | Shannon Channel Capacity of AWGN Channel. |
| [`awgn_channel.py`](09_AWGN_and_Channel_Modeling/awgn_channel.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/awgn_channel.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/awgn_channel.png) | Simulation script. |
| [`ber_vs_snr_bpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_bpsk.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_bpsk.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_bpsk.png) | Simulation script. |
| [`ber_vs_snr_qpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_qpsk.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_qpsk.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_qpsk.png) | Simulation script. |
| [`channel_estimation.py`](09_AWGN_and_Channel_Modeling/channel_estimation.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/channel_estimation.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/channel_estimation.png) | Pilot-based Channel Estimation (LS vs. MMSE). |
| [`multipath_channel.py`](09_AWGN_and_Channel_Modeling/multipath_channel.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/multipath_channel.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/multipath_channel.png) | Multipath Channel Simulation and Frequency Selective Fading. |
| [`rayleigh_fading.py`](09_AWGN_and_Channel_Modeling/rayleigh_fading.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/rayleigh_fading.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/rayleigh_fading.png) | Simulation script. |
| [`rician_fading.py`](09_AWGN_and_Channel_Modeling/rician_fading.py) | [Log](09_AWGN_and_Channel_Modeling/outputs/rician_fading.txt) | [Plot](09_AWGN_and_Channel_Modeling/outputs/rician_fading.png) | Simulation script. |

### 10. Multiplexing and Multiple Access

Folder path: [`10_Multiplexing_and_Multiple_Access`](10_Multiplexing_and_Multiple_Access)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`aloha_simulation.py`](10_Multiplexing_and_Multiple_Access/aloha_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/aloha_simulation.txt) | [Plot](10_Multiplexing_and_Multiple_Access/outputs/aloha_simulation.png) | Pure and Slotted ALOHA Multiple Access Throughput. |
| [`cdma_simulation.py`](10_Multiplexing_and_Multiple_Access/cdma_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/cdma_simulation.txt) | - | Simulation script. |
| [`fdm_simulation.py`](10_Multiplexing_and_Multiple_Access/fdm_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/fdm_simulation.txt) | [Plot](10_Multiplexing_and_Multiple_Access/outputs/fdm_simulation.png) | Simulation script. |
| [`ofdm_simulation.py`](10_Multiplexing_and_Multiple_Access/ofdm_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/ofdm_simulation.txt) | [Plot](10_Multiplexing_and_Multiple_Access/outputs/ofdm_simulation.png) | Simulation script. |
| [`tdm_simulation.py`](10_Multiplexing_and_Multiple_Access/tdm_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/tdm_simulation.txt) | [Plot](10_Multiplexing_and_Multiple_Access/outputs/tdm_simulation.png) | Simulation script. |
| [`wdm_simulation.py`](10_Multiplexing_and_Multiple_Access/wdm_simulation.py) | [Log](10_Multiplexing_and_Multiple_Access/outputs/wdm_simulation.txt) | [Plot](10_Multiplexing_and_Multiple_Access/outputs/wdm_simulation.png) | Wavelength Division Multiplexing (WDM) Simulation. |

### 11. Transmitter and Receiver Design

Folder path: [`11_Transmitter_and_Receiver_Design`](11_Transmitter_and_Receiver_Design)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`agc_automatic_gain_control.py`](11_Transmitter_and_Receiver_Design/agc_automatic_gain_control.py) | [Log](11_Transmitter_and_Receiver_Design/outputs/agc_automatic_gain_control.txt) | [Plot](11_Transmitter_and_Receiver_Design/outputs/agc_automatic_gain_control.png) | Automatic Gain Control (AGC) simulation. |
| [`direct_conversion_receiver.py`](11_Transmitter_and_Receiver_Design/direct_conversion_receiver.py) | [Log](11_Transmitter_and_Receiver_Design/outputs/direct_conversion_receiver.txt) | [Plot](11_Transmitter_and_Receiver_Design/outputs/direct_conversion_receiver.png) | Direct-conversion (zero-IF) receiver simulation. |
| [`pll_phase_locked_loop.py`](11_Transmitter_and_Receiver_Design/pll_phase_locked_loop.py) | [Log](11_Transmitter_and_Receiver_Design/outputs/pll_phase_locked_loop.txt) | [Plot](11_Transmitter_and_Receiver_Design/outputs/pll_phase_locked_loop.png) | Phase-Locked Loop (PLL) simulation. |
| [`superheterodyne_receiver.py`](11_Transmitter_and_Receiver_Design/superheterodyne_receiver.py) | [Log](11_Transmitter_and_Receiver_Design/outputs/superheterodyne_receiver.txt) | [Plot](11_Transmitter_and_Receiver_Design/outputs/superheterodyne_receiver.png) | Simulation script. |
| [`transmitter_architecture.py`](11_Transmitter_and_Receiver_Design/transmitter_architecture.py) | [Log](11_Transmitter_and_Receiver_Design/outputs/transmitter_architecture.txt) | [Plot](11_Transmitter_and_Receiver_Design/outputs/transmitter_architecture.png) | Transmitter architecture simulation. |

### 12. Spread Spectrum Communication

Folder path: [`12_Spread_Spectrum_Communication`](12_Spread_Spectrum_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`dsss_direct_sequence.py`](12_Spread_Spectrum_Communication/dsss_direct_sequence.py) | [Log](12_Spread_Spectrum_Communication/outputs/dsss_direct_sequence.txt) | [Plot](12_Spread_Spectrum_Communication/outputs/dsss_direct_sequence.png) | Direct Sequence Spread Spectrum (DSSS) simulation. |
| [`fhss_frequency_hopping.py`](12_Spread_Spectrum_Communication/fhss_frequency_hopping.py) | [Log](12_Spread_Spectrum_Communication/outputs/fhss_frequency_hopping.txt) | [Plot](12_Spread_Spectrum_Communication/outputs/fhss_frequency_hopping.png) | Frequency-Hopping Spread Spectrum (FHSS) simulation. |
| [`pn_sequence_generator.py`](12_Spread_Spectrum_Communication/pn_sequence_generator.py) | [Log](12_Spread_Spectrum_Communication/outputs/pn_sequence_generator.txt) | [Plot](12_Spread_Spectrum_Communication/outputs/pn_sequence_generator.png) | PN (Pseudo-Noise) sequence generator using LFSR. |
| [`processing_gain.py`](12_Spread_Spectrum_Communication/processing_gain.py) | [Log](12_Spread_Spectrum_Communication/outputs/processing_gain.txt) | [Plot](12_Spread_Spectrum_Communication/outputs/processing_gain.png) | Processing gain and jamming margin in spread spectrum systems. |

### 13. DSP for Communication

Folder path: [`13_DSP_for_Communication`](13_DSP_for_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`correlation_receiver.py`](13_DSP_for_Communication/correlation_receiver.py) | [Log](13_DSP_for_Communication/outputs/correlation_receiver.txt) | [Plot](13_DSP_for_Communication/outputs/correlation_receiver.png) | Simulation script. |
| [`digital_filters_fir_iir.py`](13_DSP_for_Communication/digital_filters_fir_iir.py) | [Log](13_DSP_for_Communication/outputs/digital_filters_fir_iir.txt) | [Plot](13_DSP_for_Communication/outputs/digital_filters_fir_iir.png) | Simulation script. |
| [`equalization.py`](13_DSP_for_Communication/equalization.py) | [Log](13_DSP_for_Communication/outputs/equalization.txt) | [Plot](13_DSP_for_Communication/outputs/equalization.png) | Simulation script. |
| [`matched_filter.py`](13_DSP_for_Communication/matched_filter.py) | [Log](13_DSP_for_Communication/outputs/matched_filter.txt) | [Plot](13_DSP_for_Communication/outputs/matched_filter.png) | Simulation script. |

### 14. Antenna and Wave Propagation

Folder path: [`14_Antenna_and_Wave_Propagation`](14_Antenna_and_Wave_Propagation)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`friis_transmission_equation.py`](14_Antenna_and_Wave_Propagation/friis_transmission_equation.py) | [Log](14_Antenna_and_Wave_Propagation/outputs/friis_transmission_equation.txt) | [Plot](14_Antenna_and_Wave_Propagation/outputs/friis_transmission_equation.png) | Simulation script. |
| [`ground_wave_propagation.py`](14_Antenna_and_Wave_Propagation/ground_wave_propagation.py) | [Log](14_Antenna_and_Wave_Propagation/outputs/ground_wave_propagation.txt) | [Plot](14_Antenna_and_Wave_Propagation/outputs/ground_wave_propagation.png) | Simulation script. |
| [`link_budget_calculator.py`](14_Antenna_and_Wave_Propagation/link_budget_calculator.py) | [Log](14_Antenna_and_Wave_Propagation/outputs/link_budget_calculator.txt) | - | Simulation script. |
| [`radiation_pattern.py`](14_Antenna_and_Wave_Propagation/radiation_pattern.py) | [Log](14_Antenna_and_Wave_Propagation/outputs/radiation_pattern.txt) | [Plot](14_Antenna_and_Wave_Propagation/outputs/radiation_pattern.png) | Simulation script. |

### 15. Optical Communication

Folder path: [`15_Optical_Communication`](15_Optical_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`ber_optical_link.py`](15_Optical_Communication/ber_optical_link.py) | [Log](15_Optical_Communication/outputs/ber_optical_link.txt) | [Plot](15_Optical_Communication/outputs/ber_optical_link.png) | Simulation script. |
| [`dispersion_analysis.py`](15_Optical_Communication/dispersion_analysis.py) | [Log](15_Optical_Communication/outputs/dispersion_analysis.txt) | [Plot](15_Optical_Communication/outputs/dispersion_analysis.png) | Optical Fiber Dispersion Analysis. |
| [`fiber_attenuation.py`](15_Optical_Communication/fiber_attenuation.py) | [Log](15_Optical_Communication/outputs/fiber_attenuation.txt) | [Plot](15_Optical_Communication/outputs/fiber_attenuation.png) | Simulation script. |
| [`numerical_aperture.py`](15_Optical_Communication/numerical_aperture.py) | [Log](15_Optical_Communication/outputs/numerical_aperture.txt) | - | Simulation script. |
| [`optical_link_budget.py`](15_Optical_Communication/optical_link_budget.py) | [Log](15_Optical_Communication/outputs/optical_link_budget.txt) | [Plot](15_Optical_Communication/outputs/optical_link_budget.png) | Optical Link Power Budget Design. |

### 16. Satellite Communication

Folder path: [`16_Satellite_Communication`](16_Satellite_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`doppler_shift_satellite.py`](16_Satellite_Communication/doppler_shift_satellite.py) | [Log](16_Satellite_Communication/outputs/doppler_shift_satellite.txt) | [Plot](16_Satellite_Communication/outputs/doppler_shift_satellite.png) | Simulation script. |
| [`link_budget_satellite.py`](16_Satellite_Communication/link_budget_satellite.py) | [Log](16_Satellite_Communication/outputs/link_budget_satellite.txt) | - | Simulation script. |
| [`orbital_parameters.py`](16_Satellite_Communication/orbital_parameters.py) | [Log](16_Satellite_Communication/outputs/orbital_parameters.txt) | - | Simulation script. |

### 17. Wireless and Mobile Communication

Folder path: [`17_Wireless_and_Mobile_Communication`](17_Wireless_and_Mobile_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`cellular_frequency_reuse.py`](17_Wireless_and_Mobile_Communication/cellular_frequency_reuse.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/cellular_frequency_reuse.txt) | [Plot](17_Wireless_and_Mobile_Communication/outputs/cellular_frequency_reuse.png) | Simulation script. |
| [`diversity_techniques.py`](17_Wireless_and_Mobile_Communication/diversity_techniques.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/diversity_techniques.txt) | [Plot](17_Wireless_and_Mobile_Communication/outputs/diversity_techniques.png) | Wireless Receiver Diversity Combining Techniques. |
| [`handoff_simulation.py`](17_Wireless_and_Mobile_Communication/handoff_simulation.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/handoff_simulation.txt) | [Plot](17_Wireless_and_Mobile_Communication/outputs/handoff_simulation.png) | Simulation script. |
| [`mimo_simulation.py`](17_Wireless_and_Mobile_Communication/mimo_simulation.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/mimo_simulation.txt) | - | Simulation script. |
| [`ofdm_wireless.py`](17_Wireless_and_Mobile_Communication/ofdm_wireless.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/ofdm_wireless.txt) | [Plot](17_Wireless_and_Mobile_Communication/outputs/ofdm_wireless.png) | OFDM Wireless Transmission with Cyclic Prefix. |
| [`path_loss_models.py`](17_Wireless_and_Mobile_Communication/path_loss_models.py) | [Log](17_Wireless_and_Mobile_Communication/outputs/path_loss_models.txt) | [Plot](17_Wireless_and_Mobile_Communication/outputs/path_loss_models.png) | Simulation script. |

### 18. Network Protocols and Data Link

Folder path: [`18_Network_Protocols_and_Data_Link`](18_Network_Protocols_and_Data_Link)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`arq_protocols.py`](18_Network_Protocols_and_Data_Link/arq_protocols.py) | [Log](18_Network_Protocols_and_Data_Link/outputs/arq_protocols.txt) | [Plot](18_Network_Protocols_and_Data_Link/outputs/arq_protocols.png) | ARQ (Automatic Repeat reQuest) protocol simulation. |
| [`error_detection_protocols.py`](18_Network_Protocols_and_Data_Link/error_detection_protocols.py) | [Log](18_Network_Protocols_and_Data_Link/outputs/error_detection_protocols.txt) | [Plot](18_Network_Protocols_and_Data_Link/outputs/error_detection_protocols.png) | Error detection at the data-link layer. |
| [`flow_control.py`](18_Network_Protocols_and_Data_Link/flow_control.py) | [Log](18_Network_Protocols_and_Data_Link/outputs/flow_control.txt) | [Plot](18_Network_Protocols_and_Data_Link/outputs/flow_control.png) | Sliding window flow control simulation. |

### 19. Radar Communication

Folder path: [`19_Radar_Communication`](19_Radar_Communication)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`doppler_radar.py`](19_Radar_Communication/doppler_radar.py) | [Log](19_Radar_Communication/outputs/doppler_radar.txt) | [Plot](19_Radar_Communication/outputs/doppler_radar.png) | Doppler radar simulation for moving-target velocity estimation. |
| [`pulse_compression.py`](19_Radar_Communication/pulse_compression.py) | [Log](19_Radar_Communication/outputs/pulse_compression.txt) | [Plot](19_Radar_Communication/outputs/pulse_compression.png) | Linear FM (chirp) pulse compression simulation. |
| [`radar_range_equation.py`](19_Radar_Communication/radar_range_equation.py) | [Log](19_Radar_Communication/outputs/radar_range_equation.txt) | [Plot](19_Radar_Communication/outputs/radar_range_equation.png) | Radar range equation calculation and detection analysis. |

### 20. Emerging Technologies

Folder path: [`20_Emerging_Technologies`](20_Emerging_Technologies)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`5g_nr_basics.py`](20_Emerging_Technologies/5g_nr_basics.py) | [Log](20_Emerging_Technologies/outputs/5g_nr_basics.txt) | [Plot](20_Emerging_Technologies/outputs/5g_nr_basics.png) | 5G NR (New Radio) Numerology and Slot Structure. |
| [`cognitive_radio.py`](20_Emerging_Technologies/cognitive_radio.py) | [Log](20_Emerging_Technologies/outputs/cognitive_radio.txt) | [Plot](20_Emerging_Technologies/outputs/cognitive_radio.png) | Cognitive Radio Spectrum Sensing Simulation. |
| [`massive_mimo.py`](20_Emerging_Technologies/massive_mimo.py) | [Log](20_Emerging_Technologies/outputs/massive_mimo.txt) | [Plot](20_Emerging_Technologies/outputs/massive_mimo.png) | Massive MIMO Beamforming and Precoding Simulation. |
| [`mmwave_propagation.py`](20_Emerging_Technologies/mmwave_propagation.py) | [Log](20_Emerging_Technologies/outputs/mmwave_propagation.txt) | [Plot](20_Emerging_Technologies/outputs/mmwave_propagation.png) | Millimeter Wave (mmWave) Propagation Characteristics. |

### 21. Mini Projects

Folder path: [`21_Mini_Projects`](21_Mini_Projects)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`chat_application_socket.py`](21_Mini_Projects/chat_application_socket.py) | [Log](21_Mini_Projects/outputs/chat_application_socket.txt) | - | Simulation script. |
| [`digital_filter_designer.py`](21_Mini_Projects/digital_filter_designer.py) | [Log](21_Mini_Projects/outputs/digital_filter_designer.txt) | [Plot](21_Mini_Projects/outputs/digital_filter_designer.png) | Simulation script. |
| [`dtmf_dialpad_simulator.py`](21_Mini_Projects/dtmf_dialpad_simulator.py) | [Log](21_Mini_Projects/outputs/dtmf_dialpad_simulator.txt) | [Plot](21_Mini_Projects/outputs/dtmf_dialpad_simulator.png) | Simulation script. |
| [`software_defined_radio_basics.py`](21_Mini_Projects/software_defined_radio_basics.py) | [Log](21_Mini_Projects/outputs/software_defined_radio_basics.txt) | [Plot](21_Mini_Projects/outputs/software_defined_radio_basics.png) | Simulation script. |
| [`spectrum_analyzer_gui.py`](21_Mini_Projects/spectrum_analyzer_gui.py) | [Log](21_Mini_Projects/outputs/spectrum_analyzer_gui.txt) | [Plot](21_Mini_Projects/outputs/spectrum_analyzer_gui.png) | Simulation script. |
| [`speech_signal_compression.py`](21_Mini_Projects/speech_signal_compression.py) | [Log](21_Mini_Projects/outputs/speech_signal_compression.txt) | [Plot](21_Mini_Projects/outputs/speech_signal_compression.png) | Simulation script. |

### 22. Advanced Modulation Visualizations

Folder path: [`22_Advanced_Modulation_Visualizations`](22_Advanced_Modulation_Visualizations)

| Simulation Script | Output Log | Output Plot(s) | Description |
| :--- | :--- | :--- | :--- |
| [`qam16_noise_dashboard.py`](22_Advanced_Modulation_Visualizations/qam16_noise_dashboard.py) | [Log](22_Advanced_Modulation_Visualizations/outputs/qam16_noise_dashboard.txt) | [Plot](22_Advanced_Modulation_Visualizations/outputs/qam16_noise_dashboard.png) | Simulation script. |
| [`qam_order_comparison.py`](22_Advanced_Modulation_Visualizations/qam_order_comparison.py) | [Log](22_Advanced_Modulation_Visualizations/outputs/qam_order_comparison.txt) | [Plot](22_Advanced_Modulation_Visualizations/outputs/qam_order_comparison.png) | Simulation script. |
| [`qpsk_ber_constellation_dashboard.py`](22_Advanced_Modulation_Visualizations/qpsk_ber_constellation_dashboard.py) | [Log](22_Advanced_Modulation_Visualizations/outputs/qpsk_ber_constellation_dashboard.txt) | [Plot](22_Advanced_Modulation_Visualizations/outputs/qpsk_ber_constellation_dashboard.png) | Simulation script. |


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
