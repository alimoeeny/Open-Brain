package main

type Thing struct {
	Time int64
}

type Brain struct {
	Thing
	Id       string
	Neurons  map[string]*Neuron
	Synapses map[string]*Synapse
}

type Neuron struct {
	Thing
	Id       string
	Type     string
	Synapses []*Synapse
	HillockV float64
}

type Synapse struct {
	Thing
	Id     string
	Source *Neuron
	Target *Neuron
	Weight float64
}
