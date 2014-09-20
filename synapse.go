package main

func NewSynapse(source, target *Neuron, strength float64, kernel *Kernel) *Synapse {
	s := Synapse{}
	s.Id = <-nextId
	s.Source = source
	s.Target = target
	s.Strength = strength
	s.Kernel = kernel

	source.Synapses[s.Id] = &s
	target.Synapses[s.Id] = &s
	return &s
}

func (s *Synapse) StepForward() {
	s.KernelIndex++
	if s.KernelIndex > (len(*s.Kernel) - 1) {
		s.KernelIndex = 0
	}
	// move the time forward
	s.Time++
}
