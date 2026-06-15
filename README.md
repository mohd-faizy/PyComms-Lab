
<h1>📡 PyComms</h1>

<div align="center">

<a href="https://github.com/mohd-faizy/PyComms-Lab">
  <img src="assets/head.png" alt="PyComms-Lab Banner" width="900" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
</a>

---


<p align="center">
  <strong>A comprehensive, curriculum-aligned collection of Python-based simulations for core topics in Electronics and Communication Engineering (ECE). Designed for academic learning, lab assignments, and concept visualization.</strong>
</p>

<!-- Tech Stack & Platforms -->
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://numpy.org/"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"></a>
  <a href="https://scipy.org/"><img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy"></a>
  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib"></a>
</p>

<!-- Repository Metrics -->
<p align="center">
  <a href="https://github.com/mohd-faizy/PyComms-Lab/stargazers"><img src="https://img.shields.io/github/stars/mohd-faizy/PyComms-Lab?style=for-the-badge&logo=github&logoColor=white&color=ffd700" alt="Stars"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab/issues"><img src="https://img.shields.io/github/issues/mohd-faizy/PyComms-Lab?style=for-the-badge&logo=github&logoColor=white&color=ef4444" alt="GitHub Issues"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab/commits/main"><img src="https://img.shields.io/github/last-commit/mohd-faizy/PyComms-Lab?style=for-the-badge&logo=git&logoColor=white&color=8b5cf6" alt="Last Commit"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab"><img src="https://img.shields.io/github/repo-size/mohd-faizy/PyComms-Lab?style=for-the-badge&logo=github&logoColor=white&color=6b7280" alt="Repo Size"></a>
</p>

<!-- Meta & Community -->
<p align="center">
  <a href="https://github.com/mohd-faizy"><img src="https://img.shields.io/badge/Author-mohd--faizy-red?style=for-the-badge&logo=github&logoColor=white" alt="Author"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab"><img src="https://img.shields.io/maintenance/yes/2026?style=for-the-badge&color=28a745" alt="Maintained"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab/blob/main/LICENSE"><img src="https://img.shields.io/github/license/mohd-faizy/PyComms-Lab?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=24292e" alt="License"></a>
  <a href="https://github.com/mohd-faizy/PyComms-Lab/pulls"><img src="https://img.shields.io/badge/Contributions-Welcome-0059b3?style=for-the-badge&logo=handshake&logoColor=white" alt="Contributions Welcome"></a>
</p>

</div>

---

## Curriculum

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

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`central_limit_theorem.py`](01_Probability_Random_Variables_and_Noise/central_limit_theorem.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig1.png" width="300" alt="Plot 1"> <br> <img src="01_Probability_Random_Variables_and_Noise/outputs/central_limit_theorem_fig2.png" width="300" alt="Plot 2"> | Central Limit Theorem demonstration. |
| [`gaussian_pdf_cdf.py`](01_Probability_Random_Variables_and_Noise/gaussian_pdf_cdf.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/gaussian_pdf_cdf.png" width="300" alt="Plot"> | Gaussian PDF and CDF visualization. |
| [`noise_types.py`](01_Probability_Random_Variables_and_Noise/noise_types.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/noise_types.png" width="300" alt="Plot"> | Noise types in communication systems. |
| [`probability_distributions.py`](01_Probability_Random_Variables_and_Noise/probability_distributions.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/probability_distributions.png" width="300" alt="Plot"> | Probability distributions used in communication engineering. |
| [`random_processes.py`](01_Probability_Random_Variables_and_Noise/random_processes.py) | <img src="01_Probability_Random_Variables_and_Noise/outputs/random_processes.png" width="300" alt="Plot"> | Random processes: autocorrelation and power spectral density. |

### 02. Signals and Systems

Folder path: [`02_Signals_and_Systems`](02_Signals_and_Systems)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`basic_signals_generation.py`](02_Signals_and_Systems/basic_signals_generation.py) | <img src="02_Signals_and_Systems/outputs/basic_signals_generation.png" width="300" alt="Plot"> | Simulation script. |
| [`convolution.py`](02_Signals_and_Systems/convolution.py) | <img src="02_Signals_and_Systems/outputs/convolution.png" width="300" alt="Plot"> | Simulation script. |
| [`fft_analysis.py`](02_Signals_and_Systems/fft_analysis.py) | <img src="02_Signals_and_Systems/outputs/fft_analysis.png" width="300" alt="Plot"> | Simulation script. |
| [`fourier_series.py`](02_Signals_and_Systems/fourier_series.py) | <img src="02_Signals_and_Systems/outputs/fourier_series.png" width="300" alt="Plot"> | Simulation script. |
| [`sampling_aliasing.py`](02_Signals_and_Systems/sampling_aliasing.py) | <img src="02_Signals_and_Systems/outputs/sampling_aliasing.png" width="300" alt="Plot"> | Simulation script. |

### 03. Analog Modulation

Folder path: [`03_Analog_Modulation`](03_Analog_Modulation)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`am_modulation_demodulation.py`](03_Analog_Modulation/am_modulation_demodulation.py) | <img src="03_Analog_Modulation/outputs/am_modulation_demodulation.png" width="300" alt="Plot"> | Simulation script. |
| [`fm_modulation.py`](03_Analog_Modulation/fm_modulation.py) | <img src="03_Analog_Modulation/outputs/fm_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`pm_modulation.py`](03_Analog_Modulation/pm_modulation.py) | <img src="03_Analog_Modulation/outputs/pm_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`ssb_dsb_modulation.py`](03_Analog_Modulation/ssb_dsb_modulation.py) | <img src="03_Analog_Modulation/outputs/ssb_dsb_modulation.png" width="300" alt="Plot"> | Simulation script. |

### 04. Digital Modulation

Folder path: [`04_Digital_Modulation`](04_Digital_Modulation)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`ask_modulation.py`](04_Digital_Modulation/ask_modulation.py) | <img src="04_Digital_Modulation/outputs/ask_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`constellation_diagrams.py`](04_Digital_Modulation/constellation_diagrams.py) | <img src="04_Digital_Modulation/outputs/constellation_diagrams.png" width="300" alt="Plot"> | Simulation script. |
| [`fsk_modulation.py`](04_Digital_Modulation/fsk_modulation.py) | <img src="04_Digital_Modulation/outputs/fsk_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`psk_bpsk_qpsk.py`](04_Digital_Modulation/psk_bpsk_qpsk.py) | <img src="04_Digital_Modulation/outputs/psk_bpsk_qpsk.png" width="300" alt="Plot"> | Simulation script. |
| [`qam16_modulation_demodulation.py`](04_Digital_Modulation/qam16_modulation_demodulation.py) | <img src="04_Digital_Modulation/outputs/qam16_modulation_demodulation.png" width="300" alt="Plot"> | Simulation script. |
| [`qam_modulation.py`](04_Digital_Modulation/qam_modulation.py) | <img src="04_Digital_Modulation/outputs/qam_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`qpsk_modulation_demodulation.py`](04_Digital_Modulation/qpsk_modulation_demodulation.py) | <img src="04_Digital_Modulation/outputs/qpsk_modulation_demodulation.png" width="300" alt="Plot"> | Simulation script. |

### 05. Pulse Modulation

Folder path: [`05_Pulse_Modulation`](05_Pulse_Modulation)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`adaptive_delta_modulation.py`](05_Pulse_Modulation/adaptive_delta_modulation.py) | <img src="05_Pulse_Modulation/outputs/adaptive_delta_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`delta_modulation.py`](05_Pulse_Modulation/delta_modulation.py) | <img src="05_Pulse_Modulation/outputs/delta_modulation.png" width="300" alt="Plot"> | Simulation script. |
| [`pam.py`](05_Pulse_Modulation/pam.py) | <img src="05_Pulse_Modulation/outputs/pam.png" width="300" alt="Plot"> | Simulation script. |
| [`pcm_encoding_decoding.py`](05_Pulse_Modulation/pcm_encoding_decoding.py) | <img src="05_Pulse_Modulation/outputs/pcm_encoding_decoding.png" width="300" alt="Plot"> | Simulation script. |
| [`pwm_ppm.py`](05_Pulse_Modulation/pwm_ppm.py) | <img src="05_Pulse_Modulation/outputs/pwm_ppm.png" width="300" alt="Plot"> | Simulation script. |

### 06. Information Theory and Coding

Folder path: [`06_Information_Theory_and_Coding`](06_Information_Theory_and_Coding)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`channel_capacity.py`](06_Information_Theory_and_Coding/channel_capacity.py) | <img src="06_Information_Theory_and_Coding/outputs/channel_capacity.png" width="300" alt="Plot"> | Simulation script. |
| [`entropy_calculation.py`](06_Information_Theory_and_Coding/entropy_calculation.py) | - | Simulation script. |
| [`huffman_coding.py`](06_Information_Theory_and_Coding/huffman_coding.py) | - | Simulation script. |
| [`lempel_ziv_coding.py`](06_Information_Theory_and_Coding/lempel_ziv_coding.py) | <img src="06_Information_Theory_and_Coding/outputs/lempel_ziv_coding.png" width="300" alt="Plot"> | Lempel-Ziv (LZ78) Compression Algorithm Demonstration. |
| [`mutual_information.py`](06_Information_Theory_and_Coding/mutual_information.py) | <img src="06_Information_Theory_and_Coding/outputs/mutual_information.png" width="300" alt="Plot"> | Mutual Information and BSC Channel Capacity. |
| [`rate_distortion.py`](06_Information_Theory_and_Coding/rate_distortion.py) | <img src="06_Information_Theory_and_Coding/outputs/rate_distortion.png" width="300" alt="Plot"> | Rate-Distortion Functions for Gaussian and Binary Sources. |
| [`shannon_fano_coding.py`](06_Information_Theory_and_Coding/shannon_fano_coding.py) | - | Simulation script. |
| [`source_coding_efficiency.py`](06_Information_Theory_and_Coding/source_coding_efficiency.py) | - | Simulation script. |

### 07. Error Control Coding

Folder path: [`07_Error_Control_Coding`](07_Error_Control_Coding)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`bch_code.py`](07_Error_Control_Coding/bch_code.py) | <img src="07_Error_Control_Coding/outputs/bch_code.png" width="300" alt="Plot"> | Bose-Chaudhuri-Hocquenghem (BCH) Cyclic Code. |
| [`convolutional_coding.py`](07_Error_Control_Coding/convolutional_coding.py) | - | Simulation script. |
| [`cyclic_redundancy_check.py`](07_Error_Control_Coding/cyclic_redundancy_check.py) | - | Simulation script. |
| [`hamming_code.py`](07_Error_Control_Coding/hamming_code.py) | - | Simulation script. |
| [`linear_block_codes.py`](07_Error_Control_Coding/linear_block_codes.py) | - | Simulation script. |
| [`reed_solomon_coding.py`](07_Error_Control_Coding/reed_solomon_coding.py) | <img src="07_Error_Control_Coding/outputs/reed_solomon_coding.png" width="300" alt="Plot"> | Reed-Solomon Error Control Coding. |
| [`turbo_code_basics.py`](07_Error_Control_Coding/turbo_code_basics.py) | <img src="07_Error_Control_Coding/outputs/turbo_code_basics.png" width="300" alt="Plot"> | Turbo Code Encoder and Iterative Decoder. |
| [`viterbi_decoder.py`](07_Error_Control_Coding/viterbi_decoder.py) | - | Simulation script. |

### 08. Data Transmission and Line Coding

Folder path: [`08_Data_Transmission_and_Line_Coding`](08_Data_Transmission_and_Line_Coding)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`baseband_transmission.py`](08_Data_Transmission_and_Line_Coding/baseband_transmission.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/baseband_transmission.png" width="300" alt="Plot"> | Complete baseband digital transmission system. |
| [`eye_diagram.py`](08_Data_Transmission_and_Line_Coding/eye_diagram.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/eye_diagram.png" width="300" alt="Plot"> | Eye diagram generation for baseband digital transmission. |
| [`intersymbol_interference.py`](08_Data_Transmission_and_Line_Coding/intersymbol_interference.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig1.png" width="300" alt="Plot 1"> <br> <img src="08_Data_Transmission_and_Line_Coding/outputs/intersymbol_interference_fig2.png" width="300" alt="Plot 2"> | Inter-Symbol Interference (ISI) and pulse shaping. |
| [`line_coding_schemes.py`](08_Data_Transmission_and_Line_Coding/line_coding_schemes.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/line_coding_schemes.png" width="300" alt="Plot"> | Line coding schemes used in digital data transmission. |
| [`scrambler_descrambler.py`](08_Data_Transmission_and_Line_Coding/scrambler_descrambler.py) | <img src="08_Data_Transmission_and_Line_Coding/outputs/scrambler_descrambler.png" width="300" alt="Plot"> | Scrambler and descrambler for digital data transmission. |

### 09. AWGN and Channel Modeling

Folder path: [`09_AWGN_and_Channel_Modeling`](09_AWGN_and_Channel_Modeling)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`awgn_capacity.py`](09_AWGN_and_Channel_Modeling/awgn_capacity.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/awgn_capacity.png" width="300" alt="Plot"> | Shannon Channel Capacity of AWGN Channel. |
| [`awgn_channel.py`](09_AWGN_and_Channel_Modeling/awgn_channel.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/awgn_channel.png" width="300" alt="Plot"> | Simulation script. |
| [`ber_vs_snr_bpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_bpsk.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_bpsk.png" width="300" alt="Plot"> | Simulation script. |
| [`ber_vs_snr_qpsk.py`](09_AWGN_and_Channel_Modeling/ber_vs_snr_qpsk.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/ber_vs_snr_qpsk.png" width="300" alt="Plot"> | Simulation script. |
| [`channel_estimation.py`](09_AWGN_and_Channel_Modeling/channel_estimation.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/channel_estimation.png" width="300" alt="Plot"> | Pilot-based Channel Estimation (LS vs. MMSE). |
| [`multipath_channel.py`](09_AWGN_and_Channel_Modeling/multipath_channel.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/multipath_channel.png" width="300" alt="Plot"> | Multipath Channel Simulation and Frequency Selective Fading. |
| [`rayleigh_fading.py`](09_AWGN_and_Channel_Modeling/rayleigh_fading.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/rayleigh_fading.png" width="300" alt="Plot"> | Simulation script. |
| [`rician_fading.py`](09_AWGN_and_Channel_Modeling/rician_fading.py) | <img src="09_AWGN_and_Channel_Modeling/outputs/rician_fading.png" width="300" alt="Plot"> | Simulation script. |

### 10. Multiplexing and Multiple Access

Folder path: [`10_Multiplexing_and_Multiple_Access`](10_Multiplexing_and_Multiple_Access)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`aloha_simulation.py`](10_Multiplexing_and_Multiple_Access/aloha_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/aloha_simulation.png" width="300" alt="Plot"> | Pure and Slotted ALOHA Multiple Access Throughput. |
| [`cdma_simulation.py`](10_Multiplexing_and_Multiple_Access/cdma_simulation.py) | - | Simulation script. |
| [`fdm_simulation.py`](10_Multiplexing_and_Multiple_Access/fdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/fdm_simulation.png" width="300" alt="Plot"> | Simulation script. |
| [`ofdm_simulation.py`](10_Multiplexing_and_Multiple_Access/ofdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/ofdm_simulation.png" width="300" alt="Plot"> | Simulation script. |
| [`tdm_simulation.py`](10_Multiplexing_and_Multiple_Access/tdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/tdm_simulation.png" width="300" alt="Plot"> | Simulation script. |
| [`wdm_simulation.py`](10_Multiplexing_and_Multiple_Access/wdm_simulation.py) | <img src="10_Multiplexing_and_Multiple_Access/outputs/wdm_simulation.png" width="300" alt="Plot"> | Wavelength Division Multiplexing (WDM) Simulation. |

### 11. Transmitter and Receiver Design

Folder path: [`11_Transmitter_and_Receiver_Design`](11_Transmitter_and_Receiver_Design)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`agc_automatic_gain_control.py`](11_Transmitter_and_Receiver_Design/agc_automatic_gain_control.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/agc_automatic_gain_control.png" width="300" alt="Plot"> | Automatic Gain Control (AGC) simulation. |
| [`direct_conversion_receiver.py`](11_Transmitter_and_Receiver_Design/direct_conversion_receiver.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/direct_conversion_receiver.png" width="300" alt="Plot"> | Direct-conversion (zero-IF) receiver simulation. |
| [`pll_phase_locked_loop.py`](11_Transmitter_and_Receiver_Design/pll_phase_locked_loop.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/pll_phase_locked_loop.png" width="300" alt="Plot"> | Phase-Locked Loop (PLL) simulation. |
| [`superheterodyne_receiver.py`](11_Transmitter_and_Receiver_Design/superheterodyne_receiver.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/superheterodyne_receiver.png" width="300" alt="Plot"> | Simulation script. |
| [`transmitter_architecture.py`](11_Transmitter_and_Receiver_Design/transmitter_architecture.py) | <img src="11_Transmitter_and_Receiver_Design/outputs/transmitter_architecture.png" width="300" alt="Plot"> | Transmitter architecture simulation. |

### 12. Spread Spectrum Communication

Folder path: [`12_Spread_Spectrum_Communication`](12_Spread_Spectrum_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`dsss_direct_sequence.py`](12_Spread_Spectrum_Communication/dsss_direct_sequence.py) | <img src="12_Spread_Spectrum_Communication/outputs/dsss_direct_sequence.png" width="300" alt="Plot"> | Direct Sequence Spread Spectrum (DSSS) simulation. |
| [`fhss_frequency_hopping.py`](12_Spread_Spectrum_Communication/fhss_frequency_hopping.py) | <img src="12_Spread_Spectrum_Communication/outputs/fhss_frequency_hopping.png" width="300" alt="Plot"> | Frequency-Hopping Spread Spectrum (FHSS) simulation. |
| [`pn_sequence_generator.py`](12_Spread_Spectrum_Communication/pn_sequence_generator.py) | <img src="12_Spread_Spectrum_Communication/outputs/pn_sequence_generator.png" width="300" alt="Plot"> | PN (Pseudo-Noise) sequence generator using LFSR. |
| [`processing_gain.py`](12_Spread_Spectrum_Communication/processing_gain.py) | <img src="12_Spread_Spectrum_Communication/outputs/processing_gain.png" width="300" alt="Plot"> | Processing gain and jamming margin in spread spectrum systems. |

### 13. DSP for Communication

Folder path: [`13_DSP_for_Communication`](13_DSP_for_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`correlation_receiver.py`](13_DSP_for_Communication/correlation_receiver.py) | <img src="13_DSP_for_Communication/outputs/correlation_receiver.png" width="300" alt="Plot"> | Simulation script. |
| [`digital_filters_fir_iir.py`](13_DSP_for_Communication/digital_filters_fir_iir.py) | <img src="13_DSP_for_Communication/outputs/digital_filters_fir_iir.png" width="300" alt="Plot"> | Simulation script. |
| [`equalization.py`](13_DSP_for_Communication/equalization.py) | <img src="13_DSP_for_Communication/outputs/equalization.png" width="300" alt="Plot"> | Simulation script. |
| [`matched_filter.py`](13_DSP_for_Communication/matched_filter.py) | <img src="13_DSP_for_Communication/outputs/matched_filter.png" width="300" alt="Plot"> | Simulation script. |

### 14. Antenna and Wave Propagation

Folder path: [`14_Antenna_and_Wave_Propagation`](14_Antenna_and_Wave_Propagation)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`friis_transmission_equation.py`](14_Antenna_and_Wave_Propagation/friis_transmission_equation.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/friis_transmission_equation.png" width="300" alt="Plot"> | Simulation script. |
| [`ground_wave_propagation.py`](14_Antenna_and_Wave_Propagation/ground_wave_propagation.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/ground_wave_propagation.png" width="300" alt="Plot"> | Simulation script. |
| [`link_budget_calculator.py`](14_Antenna_and_Wave_Propagation/link_budget_calculator.py) | - | Simulation script. |
| [`radiation_pattern.py`](14_Antenna_and_Wave_Propagation/radiation_pattern.py) | <img src="14_Antenna_and_Wave_Propagation/outputs/radiation_pattern.png" width="300" alt="Plot"> | Simulation script. |

### 15. Optical Communication

Folder path: [`15_Optical_Communication`](15_Optical_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`ber_optical_link.py`](15_Optical_Communication/ber_optical_link.py) | <img src="15_Optical_Communication/outputs/ber_optical_link.png" width="300" alt="Plot"> | Simulation script. |
| [`dispersion_analysis.py`](15_Optical_Communication/dispersion_analysis.py) | <img src="15_Optical_Communication/outputs/dispersion_analysis.png" width="300" alt="Plot"> | Optical Fiber Dispersion Analysis. |
| [`fiber_attenuation.py`](15_Optical_Communication/fiber_attenuation.py) | <img src="15_Optical_Communication/outputs/fiber_attenuation.png" width="300" alt="Plot"> | Simulation script. |
| [`numerical_aperture.py`](15_Optical_Communication/numerical_aperture.py) | - | Simulation script. |
| [`optical_link_budget.py`](15_Optical_Communication/optical_link_budget.py) | <img src="15_Optical_Communication/outputs/optical_link_budget.png" width="300" alt="Plot"> | Optical Link Power Budget Design. |

### 16. Satellite Communication

Folder path: [`16_Satellite_Communication`](16_Satellite_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`doppler_shift_satellite.py`](16_Satellite_Communication/doppler_shift_satellite.py) | <img src="16_Satellite_Communication/outputs/doppler_shift_satellite.png" width="300" alt="Plot"> | Simulation script. |
| [`link_budget_satellite.py`](16_Satellite_Communication/link_budget_satellite.py) | - | Simulation script. |
| [`orbital_parameters.py`](16_Satellite_Communication/orbital_parameters.py) | - | Simulation script. |

### 17. Wireless and Mobile Communication

Folder path: [`17_Wireless_and_Mobile_Communication`](17_Wireless_and_Mobile_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`cellular_frequency_reuse.py`](17_Wireless_and_Mobile_Communication/cellular_frequency_reuse.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/cellular_frequency_reuse.png" width="300" alt="Plot"> | Simulation script. |
| [`diversity_techniques.py`](17_Wireless_and_Mobile_Communication/diversity_techniques.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/diversity_techniques.png" width="300" alt="Plot"> | Wireless Receiver Diversity Combining Techniques. |
| [`handoff_simulation.py`](17_Wireless_and_Mobile_Communication/handoff_simulation.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/handoff_simulation.png" width="300" alt="Plot"> | Simulation script. |
| [`mimo_simulation.py`](17_Wireless_and_Mobile_Communication/mimo_simulation.py) | - | Simulation script. |
| [`ofdm_wireless.py`](17_Wireless_and_Mobile_Communication/ofdm_wireless.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/ofdm_wireless.png" width="300" alt="Plot"> | OFDM Wireless Transmission with Cyclic Prefix. |
| [`path_loss_models.py`](17_Wireless_and_Mobile_Communication/path_loss_models.py) | <img src="17_Wireless_and_Mobile_Communication/outputs/path_loss_models.png" width="300" alt="Plot"> | Simulation script. |

### 18. Network Protocols and Data Link

Folder path: [`18_Network_Protocols_and_Data_Link`](18_Network_Protocols_and_Data_Link)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`arq_protocols.py`](18_Network_Protocols_and_Data_Link/arq_protocols.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/arq_protocols.png" width="300" alt="Plot"> | ARQ (Automatic Repeat reQuest) protocol simulation. |
| [`error_detection_protocols.py`](18_Network_Protocols_and_Data_Link/error_detection_protocols.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/error_detection_protocols.png" width="300" alt="Plot"> | Error detection at the data-link layer. |
| [`flow_control.py`](18_Network_Protocols_and_Data_Link/flow_control.py) | <img src="18_Network_Protocols_and_Data_Link/outputs/flow_control.png" width="300" alt="Plot"> | Sliding window flow control simulation. |

### 19. Radar Communication

Folder path: [`19_Radar_Communication`](19_Radar_Communication)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`doppler_radar.py`](19_Radar_Communication/doppler_radar.py) | <img src="19_Radar_Communication/outputs/doppler_radar.png" width="300" alt="Plot"> | Doppler radar simulation for moving-target velocity estimation. |
| [`pulse_compression.py`](19_Radar_Communication/pulse_compression.py) | <img src="19_Radar_Communication/outputs/pulse_compression.png" width="300" alt="Plot"> | Linear FM (chirp) pulse compression simulation. |
| [`radar_range_equation.py`](19_Radar_Communication/radar_range_equation.py) | <img src="19_Radar_Communication/outputs/radar_range_equation.png" width="300" alt="Plot"> | Radar range equation calculation and detection analysis. |

### 20. Emerging Technologies

Folder path: [`20_Emerging_Technologies`](20_Emerging_Technologies)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`5g_nr_basics.py`](20_Emerging_Technologies/5g_nr_basics.py) | <img src="20_Emerging_Technologies/outputs/5g_nr_basics.png" width="300" alt="Plot"> | 5G NR (New Radio) Numerology and Slot Structure. |
| [`cognitive_radio.py`](20_Emerging_Technologies/cognitive_radio.py) | <img src="20_Emerging_Technologies/outputs/cognitive_radio.png" width="300" alt="Plot"> | Cognitive Radio Spectrum Sensing Simulation. |
| [`massive_mimo.py`](20_Emerging_Technologies/massive_mimo.py) | <img src="20_Emerging_Technologies/outputs/massive_mimo.png" width="300" alt="Plot"> | Massive MIMO Beamforming and Precoding Simulation. |
| [`mmwave_propagation.py`](20_Emerging_Technologies/mmwave_propagation.py) | <img src="20_Emerging_Technologies/outputs/mmwave_propagation.png" width="300" alt="Plot"> | Millimeter Wave (mmWave) Propagation Characteristics. |

### 21. Mini Projects

Folder path: [`21_Mini_Projects`](21_Mini_Projects)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`chat_application_socket.py`](21_Mini_Projects/chat_application_socket.py) | - | Simulation script. |
| [`digital_filter_designer.py`](21_Mini_Projects/digital_filter_designer.py) | <img src="21_Mini_Projects/outputs/digital_filter_designer.png" width="300" alt="Plot"> | Simulation script. |
| [`dtmf_dialpad_simulator.py`](21_Mini_Projects/dtmf_dialpad_simulator.py) | <img src="21_Mini_Projects/outputs/dtmf_dialpad_simulator.png" width="300" alt="Plot"> | Simulation script. |
| [`software_defined_radio_basics.py`](21_Mini_Projects/software_defined_radio_basics.py) | <img src="21_Mini_Projects/outputs/software_defined_radio_basics.png" width="300" alt="Plot"> | Simulation script. |
| [`spectrum_analyzer_gui.py`](21_Mini_Projects/spectrum_analyzer_gui.py) | <img src="21_Mini_Projects/outputs/spectrum_analyzer_gui.png" width="300" alt="Plot"> | Simulation script. |
| [`speech_signal_compression.py`](21_Mini_Projects/speech_signal_compression.py) | <img src="21_Mini_Projects/outputs/speech_signal_compression.png" width="300" alt="Plot"> | Simulation script. |

### 22. Advanced Modulation Visualizations

Folder path: [`22_Advanced_Modulation_Visualizations`](22_Advanced_Modulation_Visualizations)

| Simulation Script | Output Plot(s) | Description |
| :--- | :--- | :--- |
| [`qam16_noise_dashboard.py`](22_Advanced_Modulation_Visualizations/qam16_noise_dashboard.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qam16_noise_dashboard.png" width="300" alt="Plot"> | Simulation script. |
| [`qam_order_comparison.py`](22_Advanced_Modulation_Visualizations/qam_order_comparison.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qam_order_comparison.png" width="300" alt="Plot"> | Simulation script. |
| [`qpsk_ber_constellation_dashboard.py`](22_Advanced_Modulation_Visualizations/qpsk_ber_constellation_dashboard.py) | <img src="22_Advanced_Modulation_Visualizations/outputs/qpsk_ber_constellation_dashboard.png" width="300" alt="Plot"> | Simulation script. |


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

---

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

---

## 🔗 Connect with me

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/F4izy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohd-faizy/)
[![Stack Exchange](https://img.shields.io/badge/Stack_Exchange-1E5397?style=for-the-badge&logo=stack-exchange&logoColor=white)](https://ai.stackexchange.com/users/36737/faizy)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mohd-faizy)

</div>
