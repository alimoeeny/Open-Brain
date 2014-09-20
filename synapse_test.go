package main

import (
	. "github.com/alimoeeny/gomega"
	"testing"
)

func Test_Synapse_stepforwrd(t *testing.T) {
	RegisterTestingT(t)

	n1 := NewNeuron(Role_input)
	n2 := NewNeuron(Role_regular)
	s := NewSynapse(n1, n2, 0.5, baseKernel())

	Ω(s.Time).Should(Equal(int64(0)))
	Ω(s.KernelIndex).Should(Equal(0))
	s.StepForward()
	Ω(s.Time).Should(Equal(int64(1)))
	Ω(s.KernelIndex).Should(Equal(1))

	s.StepForward()
	Ω(s.Time).Should(Equal(int64(2)))
	Ω(s.KernelIndex).Should(Equal(2))
	s.StepForward()
	s.StepForward()
	s.StepForward()
	s.StepForward()
	s.StepForward()
	s.StepForward()
	s.StepForward()
	s.StepForward()
	Ω(s.Time).Should(Equal(int64(10)))
	Ω(s.KernelIndex).Should(Equal(0))
	s.StepForward()
	Ω(s.Time).Should(Equal(int64(11)))
	Ω(s.KernelIndex).Should(Equal(1))
}
