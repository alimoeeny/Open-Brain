from openbrain import *
#Brain = OpenBrain()
#Brain.Experiments[-4].loadData()
#Brain.Experiments[-3].loadData()

expt1 = Experiment('Jan20', 'Dae', None, None)
expt1.loadData('/Users/ali/Desktop/psych/dae/Idisp20Jan2010.mat')


from PlotPsycho import *
PlotPsycho([expt1], 'dx', SecondVariable='Id', MergeBlocks=True)

#PlotPsycho(array([Brain.Experiments[-3],Brain.Experiments[-4]]), StimulusVariable='dx')
#PlotPsycho(array([Brain.Experiments[-3]]), StimulusVariable='dx', MergeBlocks=False)

