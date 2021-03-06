#!/usr/bin/env python

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
try:
	import LightPipes
except ImportError:
	print "LightPipes not present"
	exit()
root = Tk.Tk()
root.wm_title("Young's experiment")

m=1
nm=1e-9*m
um=1e-6*m
mm=1e-3*m
cm=1e-2*m

LP=LightPipes.Init()
wavelength = 308*nm
size=14*mm
N=100
w=5.48*mm
f1=-10*m; f2=20*m; L=10*m; Isat=1.0; alpha=1e-4; Lgain=1e4;
tx=0.0; ty=0.00000;

f = Figure(figsize = (3,3), dpi=75)
canvas = FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

F=LP.Begin(size,wavelength,N);
F=LP.RandomIntensity(2,1,F)
F=LP.RandomPhase(5,1,F);
def TheExample():
	global F
	w=float(scale_w.get())*mm
	F=LP.RectAperture(w,w,0,0,0,F);   F=LP.Gain(Isat,alpha,Lgain,F);
	F=LP.LensFresnel(f1,L,F);   F=LP.Gain(Isat,alpha,Lgain,F);
	F=LP.LensFresnel(f2,L,F);
	F=LP.Tilt(tx,ty,F);
	F=LP.Interpol(size,N,0,0,0,1,F);
	F2=LP.RectScreen(w,w,0,0,0,F);
	I=LP.Intensity(0,F2)
	plt = f.add_subplot(111,navigate=False )
	plt.imshow(I); plt.axis('off')
	canvas.show()

def _quit():
	root.quit()		# stops mainloop
	root.destroy()	# this is necessary on Windows to prevent
					# Fatal Python Error: PyEval_RestoreThread: NULL tstate
					
#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.set_message ('PIPO')

scale_w = Tk.Scale(orient='horizontal', label = 'w/mm', length = 300, from_=1.0, to=8.0, resolution = 0.1, var = w)

scale_w.pack()


scale_w.set(w/mm)


button = Tk.Button(master=root, width = 20, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

def task():
    TheExample()
    root.after(1, task)  # reschedule event in 2 seconds

root.after(1, task)
root.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
