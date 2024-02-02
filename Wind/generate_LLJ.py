def generate_LLJ(z, alpha, zjet, Cs, zr, uref, jetmax, val, const_intensity, limits = []):
    temp = []
    for i in range(0, 200000): # How many LLJs do you want to make
        if const_intensity == True:
            zj = random.normalvariate(zjet, 90)
            zref = random.normalvariate(zr, 90)
            umax = jetmax
        else:
            zj = zjet
            zref = zr
            umax = random.weibullvariate(jetmax, 5)

        brackets = 1 - np.tanh(Cs*(z-zj)/zj)**2
        ullj = (uref + umax*(brackets))*((z/zref)**alpha)

        for j in ullj:
            iavg = float('{:.2f}'.format(j))
            temp.append(iavg)

    u = [temp[i:i+len(ullj)] for i in range(0, len(temp), len(ullj))]

    windA = []
    
    if const_intensity == True:
        if len(limits) != 0:
            lim_low = find_nearest(z, limits[0])
            lim_high = find_nearest(z, limits[1])

            for ii in u:
                if np.array(ii).max() == val:
                    if list(z).index(lim_low) <= ii.index(np.array(ii).max()) <= list(z).index(lim_high):
                        windA.append(ii)
                else:
                    None
        else:
            for ii in u:
                if np.array(ii).max() == val:
                        windA.append(ii)
    else:
        if len(limits) != 0:
            lim_low = float(limits[0])
            lim_high = float(limits[1])

            for ii in u:
                if z[ii.index(np.array(ii).max())] == val:
                    if lim_low <= np.array(ii).max() <= lim_high:
                        windA.append(ii)
                else:
                    None
        else:
            for ii in u:
                if z[ii.index(np.array(ii).max())] == val:
                    windA.append(ii)

    return windA, z
  
# find_nearest is a function which finds the closest number in an array when a value is provided.
# This function is only necessary if the user is providing limits. If len(limits) == 0, this function is not used.
# The find_nearest function is not included in this repository. However, any arbitrary find_nearest function can be used here.

# example function inputs-----------------------------------------------------------------------------------
z = np.linspace(10, 570, 113) # height array, zr should be in array
alpha = 0.11 # shear exponent
zjet = 150 # jet height
Cs = 1 # Gaussian function shape parameter
zr = 150 # reference height
ur = 7 # reference velocity
jetmax = 3 # jet maximum velocity

const_intensity = True
val = 10.59 # desired constant value of either LLJ core-speed or LLJ height, approx. ur + jetmax if constant core-speed
limits = [] # limits to which heights/core-speeds to keep
#---------------------------------------------------------------------------------------------------
