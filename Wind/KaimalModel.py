def KaimalModel(f, U, z, u_star):
    fr = f*z/U
    coeff = u_star**2/f
    Su = 105*fr/(1+33*fr)**(5/3)
    Sv = 17*fr/(1+9.5*fr)**(5/3)
    Sw = 2*fr/(1+5.3*fr**(5/3))
    Suw = -14*fr/(1+9.6*fr)**(2.4)
    
    Su = Su*coeff
    Sv = Sv*coeff
    Sw = Sw*coeff
    Suw = Suw*coeff
    return Su, Sv, Sw, Suw
