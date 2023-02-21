import soundfile
import wave
import numpy as np

file_path = "sound_files/car.wav"

# Read and rewrite the file with soundfile
data, samplerate = soundfile.read(file_path)

sound = []
for i in data:
    sound.append(i[1])

def spectrum(sound):
    f = math.abs(np.fft.fft(sound))
    return f

def cepstrum(sound):
    s = spectrum(sound)
