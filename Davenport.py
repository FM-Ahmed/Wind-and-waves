import numpy as np
import matplotlib.pyplot as plt

Cu = 5 # Decay coefficient
uavg = 15 # Mean velocity 
dy = 12.5 # Separation
fs = 10
M = 15

t, f = getSamplingPara(M, fs)

fr = f*dy/uavg # Reduced frequency
davenport = np.exp((-Cu*dy*f)/uavg) # Davenport coherence model

# plotting
plt.figure(figsize = (7, 4))
plt.plot(fr, davenport, color = 'orange')
plt.ylabel('$\gamma_i$')
plt.xlabel('$f r/\overline{u}$')
plt.grid(True, 'both')
