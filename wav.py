import soundfile
import wave
import numpy as np
import matplotlib.pyplot as plt
import math

file_path = "sound_files/chord.wav"

# Read and rewrite the file with soundfile
data, samplerate = soundfile.read(file_path)

def convert(data):
    d = []
    for i in data:
        d.append(i[0])
    return d

def spectrum(data):
    f = abs(np.fft.fft(data))
    return f

def cepstrum(data):
    # convert to spectral domain
    s = spectrum(data)
    # take the log
    for index, d in enumerate(s):
        s[index] = math.log(d)
    # inverse fourier transform into cepstral domain
    c = abs(np.fft.ifft(s))
    return c

def plot(data, func):
    data = convert(data)

    N = len(data) # size of data
    T = samplerate # sampling rate
    x = np.linspace(0.0, N*T, N)
    y = data
    yf = func(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.show()

plot(data, cepstrum)
