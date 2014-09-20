package main

func NewSynapse(source, target *Neuron) *Synapse {
	s := Synapse{}
	s.Id = <-nextId
	s.Source = source
	s.Target = target
	return s
}
