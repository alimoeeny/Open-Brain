from BFileImport import *
from numpy import *
from pylab import *

def PlotRasterPlot(filename, Start=0, Finish=0):
     Expt, ExptHeader, ExptStimvals, ExptTrials = BFileImport(filename)
     offset = 200
     if Finish == 0:
         Finish = round(d['dur'].max()[0][0]/10) + offset

     rpi = zeros((ExptTrials.size, Finish - Start + offset, 3))
     for i in range(1, ExptTrials.size):
         for j in range(1, ExptTrials[i]['Spikes'].size):
             st = round(ExptTrials[i]['Spikes'][j]/10)
             if (st >= Start) & (st < Finish) :
                 rpi[i,st - Start + offset, 0] = 1.0
                 rpi[i,st - Start + offset, 1] = 1.0
                 rpi[i,st - Start + offset, 2] = 1.0

     figure,
     imshow(rpi)
     #figimage(rpi)
     show()

