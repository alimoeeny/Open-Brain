from BFileImport import BFileImport
from numpy import squeeze

ExperimentType = set(['cylinder.ABD', 'rds.OT'])


class OBDBO(object):
    """ Open Brain Data Base Object base """
    def __init__(self):
        pass
    
class Monkey(OBDBO):
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name

class Experiment(OBDBO):
    def __init__(self, name, monkeyname, experimentType, parent):
        self.parent = parent
        self.name = name
        self.monkeyName = monkeyname
        self.experimentType = experimentType

    def loadData(self):
        filename = self.parent.spikeDataPath + self.name[3:6] + '/' +  self.name
        print filename 
        a, b, c, d = BFileImport(filename)
        self.Trials = []
        for tt in d:
            self.Trials.append(Trial(tt['id'][0][0], tt, self)) 
            for dtn in tt.dtype.names:
                exec("self.Trials[-1]." + dtn + " = squeeze(tt['" + dtn + "'])")
        print 'Got ' + self.Trials.__len__().__str__() + ' trials!'

class Neuron(OBDBO):
    def __init__(self, name, experimentname, parent):
        self.parent = parent
        self.name = name
        self.experimentName = experimentname

class Trial(OBDBO):
    def __init__(self, id, data, parent):
        self.parent = parent
        self.id = id
        self.data = data

class SpikeTrain(OBDBO):
    pass

class Stimulus(OBDBO):
    pass

#################################################################################################
class OpenBrain(object):
    def __init__(self, dataPath='./', spikeDataPath='/bgc/data/dae/'):
        self.spikeDataPath = spikeDataPath
        f = open(dataPath + 'Monkeys.txt')
        allLines = f.readlines()
        self.Monkeys = [];
        for ll in allLines:
            self.Monkeys.append(Monkey(ll[0:-1], self))
        f.close()

        self.Experiments = [];
        f = open(dataPath + 'Experiments.txt')
        allLines = f.readlines()
        for ee in allLines:
            self.Experiments.append(Experiment(ee.split()[0], ee.split()[1], ee.split()[2], self))
        f.close()

        self.Neurons = [];
        f = open(dataPath + 'Neurons.txt')
        allLines = f.readlines()
        for nn in allLines: 
            self.Neurons.append(Neuron(nn.split()[0], nn.split()[1], self))
        f.close()
