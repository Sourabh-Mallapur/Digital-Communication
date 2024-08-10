## Design and Simulation of Modulation Techniques and Signal Reconstruction Methods in Python and Matlab

## Contents 
- [Implementation of Double Sideband Suppressed Carrier (DSBSC) modulation and demodulation system using Python](#implementation_of_double_sideband_suppressed_carrier_(DSBSC)_modulation_and_demodulation_system_using_python)
- [Ideal sampling and reconstruction of signals using python](#ideal_sampling_and_reconstruction_of_signals_using_python)
- [Delta Modulator Implementation in Matlab](#delta_modulator_implementation_in_matlab)
### Implementation of Double Sideband Suppressed Carrier (DSBSC) modulation and demodulation system using Python
Leveraging a product modulator for generating the DSBSC signal and a coherent demodulator for accurately retrieving the original message signal from the modulated wave.

For exmaple - generate DSBSC wave based on product modulator. Assume fc = 10kHz, fm = 500Hz, Am = 0.5v, Ac = 1v. Show the power spectrum of the modulated waveform.
![message](https://github.com/user-attachments/assets/ce72d8d7-2eb8-493d-b8b6-bbc710cee911)
![carrier](https://github.com/user-attachments/assets/474ba050-e0dd-4ff5-a5e0-83d270982cad)

The modulated wave and its spectrum is also plotted
![modulated](https://github.com/user-attachments/assets/5a48c6aa-8656-4a86-85b3-126f9dba654b)
![modulated_spectrum](https://github.com/user-attachments/assets/6a5bf865-4928-4104-8ff7-20359509d6b8)

After Modulation and Reconstruction it is observed that the envelope of the demodulated signal resembles the original signal, reconstuction is usually done with a envelope detector circuit
![demodulated](https://github.com/user-attachments/assets/8d2860a6-4aaf-4ee3-8e15-a36b86ae89f9)
![estimated demod](https://github.com/user-attachments/assets/7e47f564-f7c2-4aa8-aea2-f05b431773c3)


### Ideal sampling and reconstruction of signals using python
First continuous time signals are converted into discrete time signals. The Nyquist frequency is Determined and reconstruction of the continuous time signal is done using samples taken at a rate higher than the Nyquist frequency. 
Two signal are taken for this example - 

![image](https://github.com/user-attachments/assets/607e1d1f-9b1b-4514-8f83-6656a2b9ef81)

### Signal A - 
![image](https://github.com/user-attachments/assets/97469d53-7464-40c8-9ea1-a43089dd00a0)
![image](https://github.com/user-attachments/assets/d2ca4610-711d-44a3-8416-7c8a71a03280)
![image](https://github.com/user-attachments/assets/a325af44-0dd9-4fb2-8704-def50c4f1338)

### Signal B - 

![image](https://github.com/user-attachments/assets/ed0fdab8-241c-4671-ab37-8925585dfabd)
![image](https://github.com/user-attachments/assets/3a2e1c62-4351-42f9-b2f3-c783afd0dd65)
![image](https://github.com/user-attachments/assets/434c928b-08a6-4d06-8533-dee46c655ea3)


### Delta Modulator Implementation in Matlab
A signal is generated and delta Modulation is performed, the similarities between the plotted signal and delta modulated signals are compared
For example
![image](https://github.com/user-attachments/assets/3fe8d976-2caa-4cd6-8a71-2fbaba471e65)
delta modulation of x(t) is performed - 
### Ts = 0.01s and δ = 0.1
![untitled](https://github.com/user-attachments/assets/7bd433a8-40d1-4979-a7b6-4c522aef7a9a)
High degree of slope overload error

### Ts = 0.01s and δ = 0.2
![untitled2](https://github.com/user-attachments/assets/737af64a-122f-455d-926d-8f7645eceaec)
Looks just right

### Ts = 0.02s and δ = 0.3
![untitled2](https://github.com/user-attachments/assets/67cd527d-8de9-4ccf-9a04-8aad1b1e1d51)
Looks just right

### Ts = 0.02s and δ = 0.5
![untitled4](https://github.com/user-attachments/assets/af90781d-962e-4cba-b588-198d3f4ef12d)
We see High degree of Granular error

