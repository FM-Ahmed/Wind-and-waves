import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.ndimage import gaussian_filter

ts = np.arange(0, 50, 0.25) # time series
T = ts[2]-ts[1] # dt
fs = 1/T # sampling frequency

df = 1/ts.max()
fcutoff_high = fs/2 # high cutoff frequency
Hs = 8 # significant wave height
Tp = 11 # peak spectral period

Sfjs, Swjs, f, omega = jonswap(Hs, Tp, df, fcutoff_high)

N = len(f)
dw = omega[2]-omega[1] # d omega
amp = np.sqrt(2*Swjs*dw)

grid_points = 50
grid_size = grid_points**2

series = []
for i in range(0, grid_size):
    phase = np.random.uniform(0, 2*np.pi, N) #random phases
    eta = np.zeros_like(ts)
    for i in range(0, ts.size):
        eta[i] = np.sum(amp*np.cos((2*np.pi*f)*ts[i] + phase))
    series.append(list(eta))
    
# sea state animation
fig, ax = plt.subplots(figsize = (10, 10), subplot_kw = dict(projection = '3d'))
ax.set_zlim(-5, 5)

sec = 0
def update(sec):
    sec += 1
    waveheight = []   
    for i in range(0, grid_size):
        waveheight.append(series[i][sec])
    waveheight = np.array(waveheight).astype(float)

    x = np.linspace(0, 10, grid_points)
    y = np.linspace(0, 10, grid_points)
    x, y = np.meshgrid(x, y)
    z = waveheight.reshape(grid_points, grid_points)

    smoothed_z = gaussian_filter(z, sigma = 2)
    
    # clear previous plot
    ax.clear()
    surf = ax.plot_surface(x, y, smoothed_z, cmap = 'ocean')
    ax.set_zlim(-10, 10)
    return surf,

anim = FuncAnimation(fig, update, frames = range(0, len(ts)-1), interval = 75)
anim.save('anim.gif')
print('Animation is saved!')
