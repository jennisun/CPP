import soundfile
import wave
import numpy as np
import matplotlib.pyplot as plt

file_path = "sound_files/car.wav"

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
    s = spectrum(data)

def plot(data):
    data = convert(data)

    N = len(data)
    T = samplerate / len(data)
    x = np.linspace(0.0, N*T, N)
    y = data
    yf = spectrum(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.show()

plot(data)
