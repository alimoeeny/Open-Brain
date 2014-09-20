package main

func NewNeuron(role NeuronRole) *Neuron {
	n := Neuron{}
	n.Id = <-nextId
	n.Role = role
	n.Synapses = map[string]*Synapse{}
	return &n
}

func (n *Neuron) StepForward() {
	if n.Recording {
		n.HillockVHistory = append(n.HillockVHistory, n.HillockV)
	}
	accumulator := 0.0
	for _, s := range n.Synapses {
		if s.Target.Id == n.Id {
			s.StepForward()
			k := *s.Kernel
			accumulator += s.Source.HillockV * k[s.KernelIndex]
		}
		n.HillockV = accumulator
	}
	// move the time forward
	n.Time++
}
