from BFileImport import BFileImport
from numpy import *
from couchquery import *

ExperimentType = set(['cylinder.ABD', 'rds.OT'])
OBPlotColors = ['red', 'blue', 'green', 'black', 'magenta', 'cyan', 'yellow']
OBPlotMarkers = [ '+', '*', '1', '2', '3', '4', '<', '>', 'D', 'H', '^', '_', 'd', 'h', 'o', 'p', 's', 'v', 'x', '|', 'TICKUP', 'TICKDOWN', 'TICKLEFT', 'TICKRIGHT']


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
        self.dataLoaded = False
        self.Trials = []

    def getData(self, dbname='openbrain'):
        ''' Get the data from couchdb'''
	obdb = Database('http://'+ self.parent.couchdbServerName + ':' + self.parent.couchdbServerPort.__str__() + '/' + dbname + '/')
	print self.name	
	Expt = obdb.views.experiments.by_name(key=self.name)
	exIt = Expt[0].iterkeys()
        for sv in exIt:
            if sv in set(['or', 'and', 'if', 'in', 'is', 'Name']):
                exec("self." + sv.upper() + " = Expt[0]['" + sv + "'] + 0.0")
            else:
		if sv <> 'Trials':
	            try:
        	        exec("self." + sv + " = Expt[0]['" + sv + "'] + 0.0")
        	    except:
        	        exec("self." + sv + " = Expt[0]['" + sv + "']")
 
	trials = Expt[0]['Trials']
        self.Trials = []
	for i in range(0,trials.__len__()):	
	    #print trials[i.__str__()]['id']
            self.Trials.append(Trial()) #self)) 
            for dtn in trials[i.__str__()]:
		dtn1 = dtn
            	if dtn in set(['or', 'and', 'if', 'in', 'is']):
		    dtn1 = dtn.upper()		
		try:
                    exec("self.Trials[-1]." + dtn1 + " = trials[i.__str__()]['" + dtn + "'] + 0.0")
                except:
                    exec("self.Trials[-1]." + dtn1 + " = trials[i.__str__()]['" + dtn + "']")
                
        print 'Got ' + self.Trials.__len__().__str__() + ' trials! in ' #+ self.BlockStart.__len__().__str__() + ' Blocks'
        self.dataLoaded = True







## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    def loadData(self, fileName=None):
        if (fileName == None) :
            fileName = self.parent.spikeDataPath + self.name[3:6] + '/' +  self.name
        print fileName 
        a, b, c, d = BFileImport(fileName)
 
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
            self.Trials.append(Trial()) #self)) 
            for dtn in tt.dtype.names:
		dtn1 = dtn
            	if dtn in set(['or', 'and', 'if', 'in', 'is']):
		    dtn1 = dtn.upper()		
		try:
                    exec("self.Trials[-1]." + dtn1 + " = squeeze(tt['" + dtn + "']) + 0.0")
                except:
                    exec("self.Trials[-1]." + dtn1 + " = squeeze(tt['" + dtn + "'])")
                
        print 'Got ' + self.Trials.__len__().__str__() + ' trials! in ' + self.BlockStart[0].__len__().__str__() + ' Blocks'
        self.dataLoaded = True

    def TrialDuration(self):
        durations = []
        for i in range(0, self.Trials.__len__()):
            durations.append(self.Trials[i].dur)
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

    def getTrialsWith(self, CategorizeBy, catValue, operator=None, nextVariable=None, nextValue=None, nextOperator=None):
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
                if operator==None:
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) == catValue :
                        r.append(i)
                elif operator=="greaterthan":
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) > catValue :
                        r.append(i)
                elif operator=="lessthan":
                    if eval('self.Trials[' + i.__str__() + '].' + CategorizeBy ) < catValue :
                        r.append(i)
        if (nextVariable!=None):
            rr = []
            for i in range(r.__len__()):
                if nextOperator==None:
#                    print 'self.Trials[' + r[i].__str__() + '].' + nextVariable
#                    print eval('self.Trials[' + r[i].__str__() + '].' + nextVariable)
                    if eval('self.Trials[' + r[i].__str__() + '].' + nextVariable ) == nextValue :
                        rr.append(r[i])
                elif nextOperator=="greaterthan":
                    if eval('self.Trials[' + r[i].__str__() + '].' + nextVariable ) > nextValue :
                        rr.append(r[i])
                elif nextOperator=="lessthan":
                    if eval('self.Trials[' + r[i].__str__() + '].' + nextVariable ) < nextValue :
                        rr.append(r[i])
            r = rr
        return r

class Neuron(OBDBO):
    def __init__(self, name, experimentname, parent):
        self.parent = parent
        self.name = name
        self.experimentName = experimentname

class Trial(OBDBO):
    def __init__(self): #, parent):
        #self.parent = parent
        self.dur = 0
        self.Spikes = []

class SpikeTrain(OBDBO):
    pass

class Stimulus(OBDBO):
    pass

#################################################################################################
class OpenBrain(object):
    def __init__(self, dataPath='./', spikeDataPath='/bgc/data/dae/', couchdbServerName='10.211.55.2', couchdbServerPort=5984):
        self.spikeDataPath = spikeDataPath
	self.couchdbServerName = couchdbServerName
	self.couchdbServerPort = couchdbServerPort
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
            try:
                self.Experiments.append(Experiment(ee.split()[0], ee.split()[1], ee.split()[2], self))
                print "We have:" + ee
            except:
                print "what's this" + ee + " ?!"
        f.close()

        self.Neurons = [];
        f = open(dataPath + 'Neurons.txt')
        allLines = f.readlines()
        for nn in allLines: 
            self.Neurons.append(Neuron(nn.split()[0], nn.split()[1], self))
        f.close()
