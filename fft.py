# https://towardsdatascience.com/fast-fourier-transform-937926e591cb

import numpy as np

def dft(x):
    x = np.asarray(x, dtype=float) # convert x to array
    N = x.shape[0] # length of x
    n = np.arange(N) # evenly spaced numbers from 0 to N (with step 1)
    k = n.reshape((N, 1)) #reshapes n to be Nx1 matrix
    M = np.exp(-2j * np.pi * k * n / N) #dft formula
    return np.dot(M, x) #dft formula

def fft(x):
    x = np.asarray(x, dtype=float) # convert x to array
    N = x.shape[0] # length of x
    if len(x) == 1:
        return dft(x)
    elif len(x) % 2 != 0:
        return("not power of 2")
    else:
        e = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([fft(x[::2]) + e[:int(N/2)] * fft(x[1::2]),
                               fft(x[::2]) + e[int(N/2):] * fft(x[1::2])])


x = np.random.random(256)
print(np.allclose(fft(x), np.fft.fft(x)))
