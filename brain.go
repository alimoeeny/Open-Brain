package main

import ()

func peaBrain() Brain {
	neuronsCount := 10
	b := Brain{}
	b.Id = <-nextId
	b.Neurons = map[string]*Neuron{}
	b.Synapses = map[string]*Synapse{}
	for i := 0; i < neuronsCount; i++ {
		n := NewNeuron()
		b.Neurons[n.Id] = n
	}
	for _, nS := range b.Neurons {
		for _, nT := range b.Neurons {
			s := NewSynapse(nS, nT)
			b.Synapses[s.Id] = s
		}
	}

	return b
}
