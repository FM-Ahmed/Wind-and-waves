fs = 10
M = 15

t, f = getSamplingPara(M, fs)

Nyy = 7
Nz = 7
ymin = -300
ymax = 300
zmin = 1
zmax = zmin+300
y = np.linspace(ymin, ymax, Nyy)
z = np.linspace(zmin, zmax, Nz)
[Y, Z] = np.meshgrid(y, z)

u_star = 0.8
kappa = 0.4
z0 = 0.03
U = u_star/kappa*np.log(Z/z0)

U = U.reshape(-1, 1)
Z = Z.reshape(-1, 1)
Y = Y.reshape(-1, 1)

Nf = len(f)
Nz = len(Z)

Su = np.zeros((Nz, Nf))
Sv = np.zeros((Nz, Nf))
Sw = np.zeros((Nz, Nf))
Suw = np.zeros((Nz, Nf))

n = kappa*U/(2*np.pi)
fr = n*z/U

for jj in range(Nz):
    Su[jj, :], Sv[jj, :], Sw[jj, :], Suw[jj, :] = KaimalModel(f, U[jj], Z[jj], u_star)
    
ind = np.argmin(np.abs(Z-150)) # spectrum at (closest to) 150 m
n = kappa*U/(2*np.pi)
plt.figure(figsize = (7, 4))
plt.semilogx(f*Z[ind]/U[ind], f*Su[ind, :]/u_star**2, label = '$fS_u/u_*^2$')
plt.semilogx(f*Z[ind]/U[ind], f*Sv[ind, :]/u_star**2, label = '$fS_v/u_*^2$')
plt.semilogx(f*Z[ind]/U[ind], f*Sw[ind, :]/u_star**2, label = '$fS_w/u_*^2$')
plt.semilogx(f*Z[ind]/U[ind], f*Suw[ind, :]/u_star**2, label = '$fS_{uw}/u_*^2$')
plt.grid(True, 'both')
plt.ylabel('$fS_i/u_*^2$')
plt.xlabel('$f z/\overline{u}$')
plt.legend(loc = 'best')
