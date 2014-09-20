from numpy import *
from pylab import *
from openbrain import *

def PlotRaster(experiments, Start=0, Finish=0, CategorizeBy=None, filename=None):
    """ PlotRaster(experiments, Start=0, Finish=0, CategorizeBy=None, filename=None) Gets a numpy ARRAY of OpenBrain.experiments and plots their Raster Plots. """
    for expt in experiments:
	offset = 200
     	if Finish == 0:
        	Finish = round(d['dur'].max()[0][0]/10) + offset

     	rpi = zeros((size(expt.Trials), Finish - Start + offset, 3))
     	for i in range(0, size(expt.Trials)):
        	for j in range(0, size(expt.Trials[i].Spikes)):
             		st = round(expt.Trials[i].Spikes[j]/10.0)
             	if (st >= Start) & (st < Finish) :
			rpi[i-1:i+1,st-1:st+1,0] = 1.0
			rpi[i-1:i+1,st-1:st+1,1] = 1.0
			rpi[i-1:i+1,st-1:st+1,2] = 1.0 
                	#rpi[i,st - Start + offset, 0] = 1.0
                 	#rpi[i,st - Start + offset, 1] = 1.0
                 	#rpi[i,st - Start + offset, 2] = 1.0

    DPI=80
    figsz = (rpi.shape[1]/80.0,rpi.shape[0]/80.0)
    print figsz
    figure(figsize=(figsz), dpi=DPI)
    imshow(rpi, aspect=None, interpolation='bilinear', cmap=cm.gray, origin='lower', extent=[rpi.shape[1],0,rpi.shape[0],0])
    #print "Plotted {0}".format(expt.name)
    print rpi.shape
    if filename == None:
        show()
    else:
        savefig(filename)

