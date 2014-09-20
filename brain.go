package main

import (
	"log"
)

func peaBrain() Brain {
	neuronsCount := 10
	b := Brain{}
	b.Id = <-nextId
	for i := 0; i < neuronsCount; i++ {
		n := NewNeuron()
		b.Neurons[n.Id] = n
	}
	for idS, nS := range b.Neurons {
		for idT, nT := range b.Neurons {
			s := NewSynaps(nS, nT)
			b.Synapses[s.Id] = s
		}
	}

	return b
}
