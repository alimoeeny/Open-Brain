package main

import (
	"fmt"
)

func (b *Brain) InputNeurons() map[string]*Neuron {
	r := map[string]*Neuron{}
	for _, n := range b.Neurons {
		if n.Role == Role_input {
			r[n.Id] = n
		}
	}
	return r
}

func (b *Brain) OutputNeurons() map[string]*Neuron {
	r := map[string]*Neuron{}
	for _, n := range b.Neurons {
		if n.Role == Role_output {
			r[n.Id] = n
		}
	}
	return r
}

func (b *Brain) RegularNeurons() map[string]*Neuron {
	r := map[string]*Neuron{}
	for _, n := range b.Neurons {
		if n.Role == Role_regular {
			r[n.Id] = n
		}
	}
	return r
}

func (b Brain) String() string {
	return fmt.Sprintf("Brain: %d input, %d regular, %d output neuroons, %d synapses", len(b.InputNeurons()), len(b.RegularNeurons()), len(b.OutputNeurons()), len(b.Synapses))
}

func NewBrain() Brain {
	b := Brain{}
	b.Id = <-nextId
	b.Status = BrainStatus_starting
	b.Neurons = map[string]*Neuron{}
	b.Synapses = map[string]*Synapse{}
	return b
}

func peaBrain() Brain {
	regularNeuronsCount := 10
	inputNeuronsCount := 3
	outputNeuronsCount := 1
	b := NewBrain()
	for i := 0; i < regularNeuronsCount; i++ {
		n := NewNeuron(Role_regular)
		b.Neurons[n.Id] = n
	}
	for i := 0; i < inputNeuronsCount; i++ {
		n := NewNeuron(Role_input)
		b.Neurons[n.Id] = n
	}
	for i := 0; i < outputNeuronsCount; i++ {
		n := NewNeuron(Role_output)
		b.Neurons[n.Id] = n
	}
	for _, nS := range b.Neurons {
		for _, nT := range b.Neurons {
			s := NewSynapse(nS, nT, 0.1, baseKernel())
			b.Synapses[s.Id] = s
		}
	}

	return b
}

func (b *Brain) Init(input map[string]float64) error {
	if len(input) != len(b.InputNeurons()) {
		return ERROR_INPUT_MISMATCH
	}
	for k := range input {
		if b.Neurons[k] == nil {
			return ERROR_INPUT_LABELED_LINE_NOT_FOUND
		}
		b.Neurons[k].HillockV = input[k]
	}
	return nil
}

func (b *Brain) StepForward() {
	// update all hillocks
	for _, n := range b.Neurons {
		n.StepForward()
	}
	// move the time forward
	b.Time++
}

func (b *Brain) AddNeuron(n *Neuron) {
	b.Neurons[n.Id] = n
	for i, s := range n.Synapses {
		b.Synapses[i] = s
	}
}
