import LightPipes as lp
import matplotlib.pyplot as plt
import numpy as np
m=1
nm=1e-9*m
um=1e-6*m
mm=1e-3*m
cm=1e-2*m

try:
    LP=lp.Init()
    
    wavelength=500*nm
    size=5.0*mm
    N=100
    R=1*mm
    z=1*m
    f=1*m
    dx=0*mm
    dy=0*mm

    F=LP.Begin(size,wavelength,N)
    F=LP.CircAperture(R, 0, 0, F)
    F=LP.Lens(f,dx,dy,F)
 

    II=np.zeros((100,100))
    F=LP.MultPhase(II,F)   
    F=LP.Forvard(z,F)
    

    I=LP.Intensity(2,F)
    #plt.imshow(I)
    plt.plot(I[N/2][:N])
    plt.show()
    
finally:
	del lp
