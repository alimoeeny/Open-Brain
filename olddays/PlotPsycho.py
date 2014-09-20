from BFileImport import *
from numpy import *
from pylab import *
from openbrain import OBPlotColors, OBPlotMarkers

def PlotPsycho(experiments, StimulusVariable, SecondVariable=None, MergeBlocks=True):
     figure(),
     for expt in experiments:
          if MergeBlocks:
               dxs = expt.getValuesFor(StimulusVariable)
               if (SecondVariable!=None):
                    sxs = expt.getValuesFor(SecondVariable)
               
               seltrials = expt.getTrialsWith(StimulusVariable, 0, operator="greaterthan")
               s = 0
               for t in array(expt.Trials)[seltrials]: 
                    s = s + t.RespDir
               if (s / seltrials.__len__()>0):
                    ResponseToPositive = 1;
                    ResponseToNegative = -1;
               else:
                    ResponseToPositive = -1;
                    ResponseToNegative = 1;

               if (SecondVariable==None):
#                    perfo = zeros((dxs.__len__(), sxs.__len__(), 3))
                    perfo = zeros((dxs.__len__(), 3))
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
               else:
                   perfo = zeros((dxs.__len__(), sxs.__len__(), 3))
                   for i in range(0, dxs.__len__()):
                         for j in range(0, sxs.__len__()):
                              seltrials = expt.getTrialsWith(StimulusVariable, dxs[i], nextVariable=SecondVariable, nextValue = sxs[j])
                              if seltrials.__len__() > 4:
                                  s = 0
                                  for t in array(expt.Trials)[seltrials]: 
                                      if t.RespDir==ResponseToPositive: 
                                          s = s + 1.0
                                  perfo[i,j,0] = s #sum(array(expt.Trials)[seltrials]['RespDir']==ResponseToPositive)
                                  s = 0.0
                                  for t in array(expt.Trials)[seltrials]: 
                                      if t.RespDir!=0: 
                                          s = s + 1.0
                                  perfo[i,j,1] = s #sum(array(expt.Trials)[seltrials]['RespDir']!=0)
                                  perfo[i,j,0] = 100.0 * perfo[i,j,0] / perfo[i,j,1]
                                  perfo[i,j,2] = 1.0 * sqrt(perfo[i,j,0] * (1 - perfo[i,j,0] / 100.0))
                                  #perfo[i,j,2] = sqrt(perfo[i,j,0] * (1 - perfo[i,j,0] / perfo[i,j,1]))
                   
                   for jj in range(0, sxs.__len__()):
                       xx = []
                       yy = []
                       yr = []
                       for ii in range(0, dxs.__len__()):
                           if(perfo[ii,jj,1]>0):
                               xx.append(dxs[ii])
                               yy.append(perfo[ii,jj,0])
                               yr.append(perfo[ii,jj,2])
                       print [xx , yy]
                       errorbar(xx, yy, yerr=yr, marker=OBPlotMarkers[jj % (sxs.__len__()/2)], mfc=OBPlotColors[jj % (sxs.__len__()/2)], mec=OBPlotColors[jj % (sxs.__len__()/2)], ms=5, mew=2, hold=True)
                       #errorbar(dxs, perfo[:,jj,0], yerr=perfo[:,jj,2], marker='o', mfc='red', mec='red', ms=5, mew=2, hold=True)

          else: # if !MergeBlocks
               for blk in expt.BlockStart[0]:
                    blockTrials = expt.getTrialsWith('block', blk)
                    dxs = expt.getValuesFor(StimulusVariable, blockTrials)
                    if ((blockTrials.__len__() < dxs.__len__() * 5) or (dxs==[])):
                         print 'NOT Enough trials in this block (' + blockTrials.__len__().__str__() + ' trials)'
                    else:
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
                         print dxs.__str__() + blockTrials.__len__().__str__() 
                         errorbar(dxs, perfo[:,0], yerr=perfo[:,2], marker='o', mfc='red', mec='red', ms=10, mew=2)

     show()

