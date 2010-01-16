from numpy import *
from pylab import *
from openbrain import *

def PlotPSTH(experiments, Start=0, Finish=0, SmoothWinLength=10, NormalizeResponses=0, CategorizeBy=None):
     """ PlotPSTH(experiments, Start=0, Finish=0, SmoothWinLength=10, NormalizeResponses=0, CategorizeBy=None) Gets a numpy ARRAY of OpenBrain.experiments and plots their average PSTHs. 
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
          
          if CategorizeBy==None:
               psthM = zeros((psth.shape[1]))
               for i in range(0, psth.shape[1]):
                    psthM[i] = psth[:,i].mean()
          else:
               catValues = expt.getValuesFor(CategorizeBy)
               psthM = zeros((catValues.__len__(), psth.shape[1]))
               for j in range(0, catValues.__len__()):
                    seltrials = expt.getTrialsWith(CategorizeBy, catValues[j])
                    for i in range(0, psth.shape[1]):
                         psthM[j,i] = psth[seltrials, i].mean()


          if NormalizeResponses==1:
               for i in range(0, psthM.shape[0]):
                    for j in range(0, psthM.shape[1]):
                         psthM[i,j] = sqrt(psthM[i,j])
          elif NormalizeResponses ==2:
               for i in range(0, psthM.shape[0]):
                    m = psthM[i,:].mean()
                    for j in range(0, psthM.shape[1]):
                         psthM[i,j] = psthM[i,j] / m
          elif NormalizeResponses == 3:
               for i in range(0, psthM.shape[0]):
                    m = psthM[i,:].mean()
                    d = psthM[i,:].max() - psthM[i,:].min()
                    for j in range(0, psthM.shape[1]):
                         psthM[i,j] = (psthM[i,j] - m ) / d

          SmoothingKernel = zeros((SmoothWinLength*2))
          SmoothingKernel[0:SmoothWinLength-1] = 1
          for i in range(0, psthM.shape[0]):
               psthM[i,:] = convolve(psthM[i,:], SmoothingKernel)[SmoothWinLength/2:SmoothWinLength/2+psthM[i,:].__len__()]
          plot(psthM.transpose())
     show()
