from openbrain import *
Brain = OpenBrain()
Brain.Experiments[-4].loadData()
Brain.Experiments[-3].loadData()

from PlotPsycho import *
#PlotPsycho(array([Brain.Experiments[-3],Brain.Experiments[-4]]), StimulusVariable='dx')
#PlotPsycho(array([Brain.Experiments[-3]]), StimulusVariable='dx', MergeBlocks=False)


from PlotPSTH import *
PlotPSTH(array([Brain.Experiments[-4]]), Start=0, Finish=1000, SmoothWinLength=20, NormalizeResponses=3, CategorizeBy='dx')

