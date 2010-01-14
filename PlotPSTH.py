from BFileImport import *
from numpy import *
from pylab import *

def PlotPSTH(filename, Start=0, Finish=0, SmoothWinLength=10):
     Expt, ExptHeader, ExptStimvals, ExptTrials = BFileImport(filename)
     offset = 200
     if Finish == 0:
         Finish = round(d['dur'].max()[0][0]/10) + offset

     psth = zeros((ExptTrials.size, Finish - Start + offset))
     for i in range(0, ExptTrials.size):
         for j in range(0, ExptTrials[i]['Spikes'].size):
             st = round(ExptTrials[i]['Spikes'][j]/10)
             if (st >= Start) & (st < Finish) :
                 psth[i,st - Start + offset] = 1.0

     psthM = zeros((psth.shape[1]))
     for i in range(0, psth.shape[1]):
          psthM[i] = psth[:,i].mean()
     
     SmoothingKernel = zeros((SmoothWinLength*2))
     SmoothingKernel[0:SmoothWinLength-1] = 1
     psthM = convolve(psthM, SmoothingKernel)

     figure(),
     plot(psthM)
     #figimage(rpi)
     show()

