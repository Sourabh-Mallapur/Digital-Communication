## Design and Simulation of Modulation Techniques and Signal Reconstruction Methods in Python and Matlab
Implementation of a Double Sideband Suppressed Carrier (DSBSC) modulation and demodulation system using Python.
Leveraging a product modulator for generating the DSBSC signal and a coherent demodulator for accurately retrieving the original message signal from the modulated wave.

For exmaple - generate DSBSC wave based on product modulator. Assume fc = 10kHz, fm = 500Hz, Am = 0.5v, Ac = 1v. Show the power spectrum of the modulated waveform.
![message](https://github.com/user-attachments/assets/ce72d8d7-2eb8-493d-b8b6-bbc710cee911)
![carrier](https://github.com/user-attachments/assets/474ba050-e0dd-4ff5-a5e0-83d270982cad)

The modulated wave and its power spectrum is also plotted
![modulated](https://github.com/user-attachments/assets/5a48c6aa-8656-4a86-85b3-126f9dba654b)
![modulated_spectrum](https://github.com/user-attachments/assets/6a5bf865-4928-4104-8ff7-20359509d6b8)

After Modulation and Reconstruction it is observed that the envelope of the demodulated signal resembles the original signal, reconstuction is usually done with a envelope detector circuit
![demodulated](https://github.com/user-attachments/assets/8d2860a6-4aaf-4ee3-8e15-a36b86ae89f9)
![estimated demod](https://github.com/user-attachments/assets/7e47f564-f7c2-4aa8-aea2-f05b431773c3)
