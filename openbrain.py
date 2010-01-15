
ExperimentType = set(['cylinder.ABD', 'rds.OT'])


class OBDBO(object):
    """ Open Brain Data Base Object base """
    def __init__(self):
        pass
    
class Monkey(OBDBO):
    def __init__(self, name):
        self.name = name

class Experiment(OBDBO):
    def __init__(self, name, experimentType, monkeyname):
        self.name = name
        self.monkeyName = monkeyname
        self.experimentType = experimentType

class Neuron(OBDBO):
    def __init__(self, name, experimentname):
        self.name = name
        self.experimentName = experimentname

class Trial(OBDBO):
    pass

class SpikeTrain(OBDBO):
    pass

class Stimulus(OBDBO):
    pass

class OpenBrain(object):
    def __init__(self, dataPath='./'):
        f = open(dataPath + 'Monkeys.txt')
        allLines = f.readlines()
        self.Monkeys = [];
        for ll in allLines:
            self.Monkeys.append(Monkey(ll[0:-1]))
        f.close()

        self.Experiments = [];
        f = open(dataPath + 'Experiments.txt')
        allLines = f.readlines()
        for ee in allLines:
            self.Experiments.append(Experiment(ee.split()[0], ee.split()[1], ee.split()[2]))
        f.close()

        self.Neurons = [];
        f = open(dataPath + 'Neurons.txt')
        allLines = f.readlines()
        for nn in allLines: 
            self.Neurons.append(Neuron(nn.split()[0], nn.split()[1]))
        f.close()
