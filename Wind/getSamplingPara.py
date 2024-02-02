import numpy as np

def getSamplingPara(M, fs):
    N = 2**M
    dt = 1/fs
    tmax = dt*N
    t = np.arange(0, N)*dt
    f0 = 1/tmax
    fc = fs/2
    f = np.arange(f0, fc+f0, f0)
    return t, f
