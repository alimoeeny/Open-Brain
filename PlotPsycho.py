from BFileImport import *
from numpy import *
from pylab import *

def PlotPsycho(filename):
     Expt, ExptHeader, ExptStimvals, ExptTrials = BFileImport(filename)
     
     dxs = unique(ExptTrials['dx'])
     perfo = zeros((dxs.size, 2))

     if (ExptTrials[ExptTrials['dx']>0]['RespDir'].mean()>0):
         ResponseToPositive = 1;
         ResponseToNegative = -1;
     else:
         ResponseToPositive = -1;
         ResponseToNegative = 1;

     for i in range(0, dxs.size):
         perfo[i,0] = sum(ExptTrials[ExptTrials['dx']==dxs[i].flat]['RespDir']==ResponseToPositive)
         perfo[i,1] = sum(ExptTrials[ExptTrials['dx']==dxs[i].flat]['RespDir']!=0)
                  
     figure(),
     plot(dxs, perfo[:,0])
     #figimage(rpi)
     show()

