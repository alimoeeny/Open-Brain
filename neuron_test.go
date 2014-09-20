package main

import (
	. "github.com/alimoeeny/gomega"
	"testing"
)

func Test_Neuron_stepforwrd(t *testing.T) {
	RegisterTestingT(t)

	n1 := NewNeuron(Role_input)
	n2 := NewNeuron(Role_regular)
	n3 := NewNeuron(Role_output)
	s1 := NewSynapse(n1, n2, 0.5, baseKernel())
	s2 := NewSynapse(n2, n2, 0.5, baseKernel())
	s3 := NewSynapse(n3, n2, 0.5, baseKernel())
	s4 := NewSynapse(n2, n3, 0.5, baseKernel())

	Ω(n2.Time).Should(Equal(int64(0)))
	Ω(s1.Time).Should(Equal(int64(0)))
	Ω(s2.Time).Should(Equal(int64(0)))
	Ω(s3.Time).Should(Equal(int64(0)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))
	n2.StepForward()
	Ω(n2.Time).Should(Equal(int64(1)))
	Ω(s1.Time).Should(Equal(int64(1)))
	Ω(s2.Time).Should(Equal(int64(1)))
	Ω(s3.Time).Should(Equal(int64(1)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))

	n2.StepForward()
	Ω(n2.Time).Should(Equal(int64(2)))
	Ω(s1.Time).Should(Equal(int64(2)))
	Ω(s2.Time).Should(Equal(int64(2)))
	Ω(s3.Time).Should(Equal(int64(2)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))

	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	n2.StepForward()
	Ω(n2.Time).Should(Equal(int64(10)))
	Ω(s1.Time).Should(Equal(int64(10)))
	Ω(s2.Time).Should(Equal(int64(10)))
	Ω(s3.Time).Should(Equal(int64(10)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))

	n2.StepForward()
	Ω(n2.Time).Should(Equal(int64(11)))
	Ω(s1.Time).Should(Equal(int64(11)))
	Ω(s2.Time).Should(Equal(int64(11)))
	Ω(s3.Time).Should(Equal(int64(11)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))
}
