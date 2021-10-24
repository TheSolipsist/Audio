from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt

samplerate = 44100
fs = 500
sec = 4

t = np.linspace(0, sec, samplerate * sec)
amplitude = 2000
fs31 = np.linspace(50, 300, samplerate * sec // 2)
fs41 = np.linspace(300, 1000, samplerate * sec // 2)

data1 = amplitude * np.sin(2 * np.pi * 3 * t) * np.sin(2 * np.pi * fs * t)
data2 = amplitude * np.sin(2 * np.pi * 55 * t)
data31 = amplitude * np.sin(2 * np.pi * fs31 * t[:len(t)//2]) 
data41 = amplitude * np.sin(2 * np.pi * fs41 * t[:len(t)//2]) 
data3 = np.concatenate((data31, data41))
data = (data1 + data2 + data3) / 3
write("example.wav", samplerate, data.astype(np.int16))
