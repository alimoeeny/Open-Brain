from openbrain import *
from BruceMat2AliCouch import BruceMat2AliCouch


Experiments = [];
f = open('Experiments.txt')
allLines = f.readlines()
for ee in allLines:
    Expt = Experiment(ee.split()[0], ee.split()[1], ee.split()[2], None);
    #Expt = Experiment('dae062.c1.cylinder.ABD.mat', 'Daedalus', 'cylinder.ABD', None)
    BruceMat2AliCouch(Expt)

f.close()



#Expt = Experiment('dae062.c1.cylinder.ABD.mat', 'Daedalus', 'cylinder.ABD', None)
#BruceMat2AliCouch(Expt)
