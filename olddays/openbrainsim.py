import numpy
from openbrain import Experiment
from openbrain import Trial

neuronIds = []
clock = 1 #in the sense of a CPU clock but in milli seconds
#theTimeNow = -1 #we are just before the big bang

class nState:
    resting=0
    spiking=1
    recovery=2

def genId():
    try:
        neuronIds.append(neuronIds[-1]+1)
    except:
        neuronIds.append(0)
    return neuronIds[-1]

class synapse(object):
    def __init__(self, n, oN, weight):
        self.neuron = n #reci
        self.otherNeuron = oN #pre synaptic neuron
        self.weight = weight

class simNeuron(object):
    def __init__(self):
        self.nId = genId()
        self.restingPotential = -65.0
        self.threshold = -60.0
        self.peakPotential = 30
        self.membranePotential = []
        self.membranePotential.append([])
        self.membranePotential[0].append(self.restingPotential)
        self.state = nState.resting
        self.synapses = []
        #global theTimeNow
        #self.timeNow = theTimeNow
        self.experiment = Experiment('expt' + self.nId.__str__(), 'android', 'plainsimulation', self)
        self.experiment.Trials.append(Trial())#self.experiment))
        #self.experiment.Trials[0].Spikes = []

    def initTrials(self, trialsCount):
        self.experiment.Trials = []
        for i in range(trialsCount):
            self.experiment.Trials.append(Trial()) #self.experiment))
            self.membranePotential.append([self.restingPotential])
    def isConnectedWith(self, otherId):
        for sy in self.synapses:
            if sy.otherNeuron.nId == otherId:
                return True
        return False

    def spike(self, trialIdx):
        """ This checks to see if this neuron should spike or not and if it should it manages the action potential"""
        if self.state == nState.resting:
            if self.membranePotential[trialIdx][-1] > self.threshold:
                self.state = nState.spiking
                self.membranePotential[trialIdx].append(self.peakPotential)
                self.experiment.Trials[trialIdx].Spikes.append(self.membranePotential[trialIdx].__len__())  #self.timeNow)
                self.experiment.Trials[trialIdx].dur = self.membranePotential[trialIdx].__len__() #self.timeNow
                print "spike" + self.membranePotential[trialIdx].__len__().__str__() # self.timeNow.__str__()
        elif self.state == nState.spiking:
            self.state = nState.recovery
            self.membranePotential[trialIdx].append(0)
        elif self.state == nState.recovery:
            self.state = nState.resting
            self.membranePotential[trialIdx].append(self.restingPotential)

    def tickAway(self, trialIdx):
        #global theTimeNow
        #if self.timeNow < theTimeNow:
        #    print "WHAT's GOING ON HERE, DON'T MESS WITH TIME"
            
        si = 0
        for sy in self.synapses:
            if sy.otherNeuron.state == nState.resting:
                si = si
            elif sy.otherNeuron.state == nState.spiking:
                si = si + sy.weight * 1.0
            elif sy.otherNeuron.state == nState.recovery:
                si = si
        self.membranePotential[trialIdx].append(self.membranePotential[trialIdx][-1] + si)
        self.spike(trialIdx)
        #self.timeNow = self.timeNow + 1

class nNet(object):
    def __init__(self, neuronCount):
        self.neurons = []
        for i in range(neuronCount):
            self.neurons.append(simNeuron())

    def fullInterConnect(self, defaultWeight):
        for n in self.neurons:
            n.synapses = []
        c = 0
        for n in self.neurons:
            for no in self.neurons:
                if n.nId != no.nId:
                    if not(n.isConnectedWith(no)):
                        n.synapses.append(synapse(n, no, defaultWeight))
                    
    def randomInterConnect(self):
        for n in self.neurons:
            n.synapses = []
        c = 0
        for n in self.neurons:
            for no in self.neurons:
                if n.nId != no.nId:
                    if not(n.isConnectedWidth(no)):
                        n.synapses.append([no.nId, numpy.random.randn()])

    def initTrials(self, tCount):
        for n in self.neurons:
            n.initTrials(tCount)

    def run(self, trialsCount, trialDuration):
        #global theTimeNow
        #theTimeNow = theTimeNow + 1
        self.initTrials(trialsCount)
        for tr in range(trialsCount):
            for i in range(trialDuration):
                for nn in self.neurons:
                    nn.tickAway(tr)



