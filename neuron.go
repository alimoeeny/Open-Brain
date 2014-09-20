package main

func NewNeuron() *Neuron {
	n := Neuron{}
	n.Id = <-nextId
	return n
}
