from scipy.io.wavfile import write
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

SAMPLERATE = 44100

def get_sound_data(sec, freq_func, amplitude):
    """Get sound data for wav file

    Args:
        sec ([type]): [description]
        freq_func ([type]): [description]
        amplitude ([type]): [description]

    Returns:
        [type]: [description]
    """
    t = np.linspace(0, sec, SAMPLERATE * sec)
    data = amplitude * np.sin(2 * np.pi * quad(0, t, freq_func))
    return data

sec = 1
freq = np.linspace(50, 70, SAMPLERATE * sec)
amplitude = np.linspace(0, 2000, SAMPLERATE * sec)
t = np.linspace(0, sec, SAMPLERATE * sec)
data = amplitude * np.sin(2*np.pi * (50 * t + 10050 * t ** 2))
# data = get_sound_data_constant(sec, 200, amplitude)
write("example.wav", SAMPLERATE, data.astype(np.int16))