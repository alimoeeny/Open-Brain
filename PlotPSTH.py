from numpy import *
from pylab import *
from openbrain import *

def PlotPSTH(experiments, Start=0, Finish=0, SmoothWinLength=10, NormalizeResponses=0):
     """ PlotPSTH(experiments, Start=0, Finish=0, SmoothWinLength=10) Gets a numpy ARRAY of OpenBrain.experiments and plots their average PSTHs. 
NormalizeResponse: 0 means no normalization, 1 means using the square root of responses (this is effectivly a variance normazliation, 2 means normalization by division by mean of responses, 3 means subtraction of mean and division by max - min 
"""
     figure(),
     for expt in experiments:
          offset = 200
          if Finish == 0:
               Finish = expt.TrialDuration + offset

          psth = zeros((expt.Trials.__len__(), Finish - Start + offset))
          for i in range(0, expt.Trials.__len__()):
               if size(expt.Trials[i].Spikes)>1:
                    for j in range(0, expt.Trials[i].Spikes.__len__()):
                         st = round(expt.Trials[i].Spikes[j]/10)
                         if (st >= Start) & (st < Finish) :
                              psth[i,st - Start + offset] = 1.0

          psthM = zeros((psth.shape[1]))
          for i in range(0, psth.shape[1]):
               psthM[i] = psth[:,i].mean()
          
          if NormalizeResponses==1:
               for i in range(0, psthM.shape[0]):
                    psthM[i] = sqrt(psthM[i])
          elif NormalizeResponses ==2:
               m = psthM.mean()
               for i in range(0, psthM.shape[0]):
                    psthM[i] = psthM[i] / m
          elif NormalizeResponses == 3:
               m = psthM.mean()
               d = psthM.max() - psthM.min()
               for i in range(0, psthM.shape[0]):
                    psthM[i] = (psthM[i] - m ) / d

          SmoothingKernel = zeros((SmoothWinLength*2))
          SmoothingKernel[0:SmoothWinLength-1] = 1
          psthM = convolve(psthM, SmoothingKernel)

          plot(psthM)
     show()
