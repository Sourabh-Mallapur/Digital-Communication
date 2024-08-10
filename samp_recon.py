import numpy as np
import matplotlib.pyplot as plt

######## Example 1 #########
fs = 0.5 # sampling frequency (Hz)
Ts = 1/fs # sampling period (s)
T = 10 # continuous time to be displayed (s)
n = np.arange(0,int(np.ceil(T/Ts))+1,1) # number of samples
t = np.arange(0,T+0.1*Ts,0.1*Ts) # continuous time (e.g., 10 times number of samples)
x = np.square(np.sinc(1/4.0*(n*Ts-5))) # sampled signal
z = np.square(np.sinc((t-5)/4.0)) # continuous time signal with higher resolution

# Plotting original signal 
plt.figure()
plt.plot(t,z) # samples versus sampling instants
plt.title("original Signal")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.show()

#### Plotting sampled signal ####
plt.figure()
plt.stem(n/fs,x) # samples versus sampling instants
plt.title("Ideal sampling output")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.show()

#### Reconstruction ####
y=np.zeros((len(t),1),float) # reconstructed signal (size = size of t)
for i in range(len(t)):
    for j in n:
        y[i] += x[j]*np.sinc((t[i]-j*Ts)/Ts) # interpolation

#### Plotting continuous time signal and the reconstructed signal ####
plt.figure(2)
plt.title("Reconstructed signal")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.plot(t,y,'b',label='x(nTs)')
plt.plot(t,z,'r',label='x(t)')
plt.legend(loc=0,fontsize=10)
plt.show()

# ######## Example 2 ############
fs= 15.0  # sampling frequency (Hz)
Ts=1/fs # sampling period (s)
T=1 # continuous time to be displayed (s)
n=np.arange(0,int(np.ceil(T/Ts))+1,1) # number of samples
t=np.arange(0,T+0.001*Ts,0.001*Ts) # continuous time (e.g., 10 times number of samples)
x=2*np.cos(2*np.pi*3*n*Ts+0.1)+2*np.cos(2*np.pi*5*n*Ts+0.2) # sampled signal
z=2*np.cos(2*np.pi*3*t+0.1)+2*np.cos(2*np.pi*5*t+0.2) # continuous time signal with higher resolution

# Plotting original signal 
plt.figure()
plt.plot(t,z) # samples versus sampling instants
plt.title("original Signal")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.show()

#### Plotting sampled signal ####
plt.figure()
plt.stem(n/fs,x) # samples versus sampling instants
plt.title("Ideal sampling output")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.show()

#### Reconstruction ####
y=np.zeros((len(t),1),float) # reconstructed signal (size = size of t)
for i in range(len(t)):
    for j in n:
        y[i] += x[j]*np.sinc((t[i]-j*Ts)/Ts) # interpolation

#### Plotting continuous time signal and the reconstructed signal ####
plt.figure(2)
plt.title("Reconstructed signal")
plt.ylabel("Magnitude")
plt.xlabel("Time")
plt.plot(t,y,'b',label='x(nTs)')
plt.plot(t,z,'r',label='x(t)')
plt.legend(loc=0,fontsize=10)
plt.show()