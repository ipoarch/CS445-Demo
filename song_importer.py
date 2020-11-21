from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

def decompose_song(filename):
    if(filename[len(filename)-3:] == 'mp3'):
        decompose_mp3(filename)
    elif(filename[len(filename)-3:] == 'wav'):
        decompose_wav(filename)
    else:
        return 0

def decompose_mp3(filename):
    return 0

def decompose_wav(filename):
    samplerate, data = wavfile.read(filename)
    print(data)

    length = data.shape[0] / samplerate
    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
    return 0