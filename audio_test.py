from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

SAMPLERATE = 44100

def get_sound_data(sec, freq_func, amplitude):
    """Get sound data for wav file

    Args:
        sec ([int]): [seconds that the sound will last for]
        freq_func ([function]): [function that takes t as input and returns frequency for that t]
        amplitude ([type]): [description]

    Returns:
        [np.array]: [description]
    """
    t = np.linspace(0, sec, SAMPLERATE * sec)
    data = np.array(t, dtype=np.int16)
    for i in range(data.size):
        data[i] = amplitude * np.sin(2 * np.pi * quad(freq_func, 0, t[i])[0])
    return data

sec = 2
amplitude = 2000
t = np.linspace(0, sec, SAMPLERATE * sec)
freq_func = lambda t: (50 + 30*abs(t-sec//2))
data = get_sound_data(sec, freq_func, amplitude)

sec = 2
amplitude = 2000
t = np.linspace(0, sec, SAMPLERATE * sec)
freq_func = lambda t: (50 - 20*abs(t-sec//2))
data += get_sound_data(sec, freq_func, amplitude)

data = data // 2
write("example.wav", SAMPLERATE, data)