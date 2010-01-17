from BFileImport import *
from numpy import *
from pylab import *


def PlotPsycho(filename):
     Expt, ExptHeader, ExptStimvals, ExptTrials = BFileImport(filename)
     
     dxs = unique(ExptTrials['dx'])
     for i in range(0,dxs.size): dxs[i] = dxs[i][0][0]
     perfo = zeros((dxs.size, 3))

     if (ExptTrials[ExptTrials['dx']>0]['RespDir'].mean()>0):
         ResponseToPositive = 1;
         ResponseToNegative = -1;
     else:
         ResponseToPositive = -1;
         ResponseToNegative = 1;

     for i in range(0, dxs.size):
         perfo[i,0] = sum(ExptTrials[ExptTrials['dx']==dxs[i].flat]['RespDir']==ResponseToPositive)
         perfo[i,1] = sum(ExptTrials[ExptTrials['dx']==dxs[i].flat]['RespDir']!=0)
         perfo[i,2] = sqrt(perfo[i,0] * (1 - perfo[i,0] / perfo[i,1]))

     figure(),
     #plot(dxs, perfo[:,0])
     errorbar(dxs, perfo[:,0], yerr=perfo[:,2], marker='o', mfc='red', mec='red', ms=10, mew=2)
     #figimage(rpi)
     show()


def PlotPsycho(experiments, StimulusVariable, MergeBlocks=True):
     figure(),
     for expt in experiments:
          dxs = expt.getValuesFor(StimulusVariable)
          perfo = zeros((dxs.__len__(), 3))

          seltrials = expt.getTrialsWith(StimulusVariable, 0, "greaterthan")
          s = 0
          for t in array(expt.Trials)[seltrials]: 
               s = s + t.RespDir
          if (s / seltrials.__len__()>0):
               ResponseToPositive = 1;
               ResponseToNegative = -1;
          else:
               ResponseToPositive = -1;
               ResponseToNegative = 1;

          for i in range(0, dxs.__len__()):
               seltrials = expt.getTrialsWith(StimulusVariable, dxs[i])
               s = 0
               for t in array(expt.Trials)[seltrials]: 
                    if t.RespDir==ResponseToPositive: 
                         s = s + 1
               perfo[i,0] = s #sum(array(expt.Trials)[seltrials]['RespDir']==ResponseToPositive)
               s = 0
               for t in array(expt.Trials)[seltrials]: 
                    if t.RespDir!=0: 
                         s = s + 1
               perfo[i,1] = s #sum(array(expt.Trials)[seltrials]['RespDir']!=0)
               perfo[i,2] = sqrt(perfo[i,0] * (1 - perfo[i,0] / perfo[i,1]))
          print dxs
          errorbar(dxs, perfo[:,0], yerr=perfo[:,2], marker='o', mfc='red', mec='red', ms=10, mew=2)
     show()

