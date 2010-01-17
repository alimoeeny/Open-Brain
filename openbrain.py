from BFileImport import BFileImport
from numpy import *

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
 
        for sv in c.dtype.names:
            if sv in set(['or', 'and', 'if', 'in', 'is']):
                exec("self." + sv.upper() + " = squeeze(c['" + sv + "']) + 0.0")
            else:
                try:
                    exec("self." + sv + " = squeeze(c['" + sv + "']) + 0.0")
                except:
                    exec("self." + sv + " = squeeze(c['" + sv + "'])")
        for sv in b.dtype.names:
            #print sv
            if sv in set(['or', 'and', 'if', 'in', 'is', 'Name']):
                try:
                    exec("self." + sv.upper() + " = squeeze(b['" + sv + "']) + 0.0")
                except:
                    exec("self." + sv.upper() + " = squeeze(b['" + sv + "'])")
            else:
                try:
                    exec("self." + sv + " = squeeze(b['" + sv + "']) + 0.0")
                except:
                    exec("self." + sv + " = squeeze(b['" + sv + "'])")

        self.Trials = []
        for tt in d:
            self.Trials.append(Trial(self)) 
            for dtn in tt.dtype.names:
                try:
                    exec("self.Trials[-1]." + dtn + " = squeeze(tt['" + dtn + "']) + 0.0")
                except:
                    exec("self.Trials[-1]." + dtn + " = squeeze(tt['" + dtn + "'])")
                
        print 'Got ' + self.Trials.__len__().__str__() + ' trials! in ' + self.BlockStart[0].__len__().__str__() + ' Blocks'


    def TrialDuration(self):
        durations = []
        for i in range(0, self.Trials.__len__()):
            durations = self.Trials[i].dur
        return median(array(durations))
    
    def getValuesFor(self, CategorizeBy, selectTrials=None):
        values = set([])
        if selectTrials==None:
            selectTrials = range(0,self.Trials.__len__())
        for i in range(0, selectTrials.__len__()):
            exec('values.add(self.Trials[' + selectTrials[i].__str__() + '].' + CategorizeBy + ')')
        a = list(values)
        a.sort()
        return a

    def getTrialsWith(self, CategorizeBy, catValue, Operator=None):
        r = []
        if (CategorizeBy.lower() == 'block'):
            blockStart = catValue
            if list(self.BlockStart[0]).index(catValue) +1 < self.BlockStart[0].__len__():
                blockEnd = self.BlockStart[0][list(self.BlockStart[0]).index(catValue)+1]
            else:
                blockEnd = self.Trials[-1].Trial + 1
            for i in range(0, self.Trials.__len__()):
                if ( self.Trials[i].Trial >=blockStart and self.Trials[i].Trial < blockEnd):
                    r.append(i)
        else:
            for i in range(0, self.Trials.__len__()):
                if Operator==None:
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) == catValue :
                        r.append(i)
                elif Operator=="greaterthan":
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) > catValue :
                        r.append(i)
                elif Operator=="lessthan":
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) < catValue :
                        r.append(i)
        return r

class Neuron(OBDBO):
    def __init__(self, name, experimentname, parent):
        self.parent = parent
        self.name = name
        self.experimentName = experimentname

class Trial(OBDBO):
    def __init__(self, parent):
        self.parent = parent

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
