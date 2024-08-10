import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

Am = 0.5      # Message signal Amplitude
Ac = 1;       # Carrier Signal Amplitude
fc = 10000;   # Message signal Frequency
fm = 500;     # Carrier Signal Frequency
N = 1e5;      # No of points for visualisation
# fs = 3 * (fm + fc);  # Sampling Frequency twice of the max frequency
fs = 20 * (fm + fc);

# Creating time Axis
time = np.arange(N)/fs
print(time)

# Generating message, carrier signals
message = Am * np.cos(2*np.pi*fm*time);
carrier = Ac * np.cos(2*np.pi*fc*time);

# plotting said signals
plt.figure(figsize=(15,3))
plt.title("Message Signal")
plt.plot(time[0:600], message[0:600])
plt.figure(figsize=(15,3))
plt.title("Carrier Signal")
plt.plot(time[0:600], carrier[0:600])

# generating modulated wave
modulated_sig = np.multiply(message, carrier)
plt.figure(figsize=(15,3))
plt.title("Modulated Signal")
plt.plot(time[0:600], modulated_sig[0:600])


# Power Spectrum
plt.figure(figsize=(7,4))
f, Pxx_den = sg.welch(modulated_sig, fs, nperseg=N)
plt.plot(f, Pxx_den)
plt.title("Power Spectrum Density [V**2/Hz]")
plt.xlim([8e3, 1.2e4])
plt.xlabel('frequency [Hz]')


plt.figure(figsize=(7,4))
f, Pxx_spec = sg.welch(modulated_sig, fs,'flattop',N)
plt.plot(f, np.sqrt(Pxx_spec))
plt.title("Linear Power Spectrum [V RMS]")
plt.xlim([8e3, 1.2e4])
plt.xlabel('frequency [Hz]')



# Coherent Demodulation
y = np.multiply(carrier, modulated_sig)  # Multiply Demodulated Signal with its Copy
plt.figure(figsize=(15,3))
plt.title("DEMODULATED Signal")
plt.plot(time[0:600], y[0:600])

# Function Definitions
def butterworth(cutoff, fs, order = 4):
  nyq = 0.5 * fs
  nor_cutoff = cutoff/nyq   # normalization of cutoff
  b, a = butter(order, nor_cutoff, btype = 'lowpass', analog = False)
  return b,a

def butter_lowpass_filter(data, cutoff, fs, order = 4):
  b, a = butterworth(cutoff, fs, order = order )
  y = lfilter(b,a,data)
  return y

order = 4     # Order of Lowpass Filter
cutoff = fm   # Cutoff Frequency of Lowpass Filter

# generation of Demodulated Signal
yt = butter_lowpass_filter(y, cutoff, fs)
plt.figure(figsize=(15,3))
plt.title("Estimated message Signal")
plt.plot(time[4400:5000], yt[4400:5000])

from scipy.fft import fft, fftfreq

yf = fft(modulated_sig/N)
xf = fftfreq(int(N), abs(1 / fs))
plt.figure(figsize=(10,5))
plt.xlim([-15000, 15000])
plt.ylim([0.05, 0.14])
plt.plot(xf, np.abs(yf))
plt.title("Spectrum of modulated Signal")
plt.show()

yf = fft(yt/N)
xf = fftfreq(int(N), abs(1 / fs))
plt.figure(figsize=(10,5))
plt.xlim([-5000, 5000])
plt.ylim([0.04, 0.1])
plt.plot(xf, np.abs(yf))
plt.title("Spectrum of Estimated Message Signal")
plt.show()
