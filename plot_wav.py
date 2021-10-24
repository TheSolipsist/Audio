from scipy.io.wavfile import read
from matplotlib import pyplot as plt

samplerate, wav_data = read("example2.wav")
plt.plot(wav_data)
plt.show()
