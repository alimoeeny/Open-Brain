#!/usr/bin/python

from openbrainsim import *
nnet = nNet(100)
nnet.fullInterConnect(0.1)

from numpy import random
for n in nnet.neurons:
	n.membranePotential[0][-1] = n.membranePotential[0][-1] + random.randn() * 20.0	
	if n.membranePotential[0][-1] > n.threshold:
		n.state = nState.spiking
		
nnet.run(10,1000)

from PlotPSTH import *
expts = []
for i in nnet.neurons:
	expts.append(i.experiment)
PlotPSTH(expts)

