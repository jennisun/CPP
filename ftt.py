# https://towardsdatascience.com/fast-fourier-transform-937926e591cb

import numpy as np

def dft(x):
    x = np.asarray(x, dtype=float) # convert x to array
    N = x.shape[0] # length of x
    n = np.arange(N) # evenly spaced numbers from 0 to N (with step 1)
    k = n.reshape((N, 1)) #reshapes n to be Nx1 matrix
    M = np.exp(-2j * np.pi * k * n / N) #dft formula
    return np.dot(M, x) #dft formula

x = np.random.random(1024)
np.allclose(dft(x), np.fft.fft(x))
