import LightPipes
import matplotlib.pyplot as plt
Pi=3.1415
m=1
nm=1e-9*m
um=1e-6*m
mm=1e-3*m
cm=1e-2*m
deg=Pi/180.0

try:
    LP=LightPipes.Init()
    
    wavelength=632.8*nm
    size=5.0*mm
    N=500
    phi=179.8*deg
    n1=1.5
    z=80*cm
    
    F=LP.Begin(size,wavelength,N)
    F=LP.Axicon(phi,n1,0,0,F)
    F=LP.Forvard(z,F)
    I=LP.Intensity(2,F)
    plt.imshow(I)
    plt.show()
    
finally:
	del LightPipes
