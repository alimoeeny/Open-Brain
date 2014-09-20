package main

import (
	. "github.com/alimoeeny/gomega"
	"testing"
)

func Test_InputNeurons(t *testing.T) {
	RegisterTestingT(t)

	b := NewBrain()
	Ω(len(b.InputNeurons())).Should(Equal(0))

	ni1 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni1.Id] = &ni1
	Ω(len(b.InputNeurons())).Should(Equal(1))

	ni2 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni2.Id] = &ni2
	Ω(len(b.InputNeurons())).Should(Equal(2))

	ni3 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni3.Id] = &ni3
	Ω(len(b.InputNeurons())).Should(Equal(2))

	ni4 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[ni4.Id] = &ni4
	Ω(len(b.InputNeurons())).Should(Equal(2))

	ni5 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni5.Id] = &ni5
	Ω(len(b.InputNeurons())).Should(Equal(2))

	ni6 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni6.Id] = &ni6
	Ω(len(b.InputNeurons())).Should(Equal(3))
}

func Test_OutputNeurons(t *testing.T) {
	RegisterTestingT(t)

	b := NewBrain()
	Ω(len(b.OutputNeurons())).Should(Equal(0))

	ni1 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni1.Id] = &ni1
	Ω(len(b.OutputNeurons())).Should(Equal(1))

	ni2 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni2.Id] = &ni2
	Ω(len(b.OutputNeurons())).Should(Equal(1))

	ni3 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni3.Id] = &ni3
	Ω(len(b.OutputNeurons())).Should(Equal(2))

	ni4 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[ni4.Id] = &ni4
	Ω(len(b.OutputNeurons())).Should(Equal(2))

	ni5 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni5.Id] = &ni5
	Ω(len(b.OutputNeurons())).Should(Equal(3))

	ni6 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni6.Id] = &ni6
	Ω(len(b.OutputNeurons())).Should(Equal(3))
}

func Test_RegularNeurons(t *testing.T) {
	RegisterTestingT(t)

	b := NewBrain()
	Ω(len(b.RegularNeurons())).Should(Equal(0))

	ni1 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni1.Id] = &ni1
	Ω(len(b.RegularNeurons())).Should(Equal(0))

	ni2 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[ni2.Id] = &ni2
	Ω(len(b.RegularNeurons())).Should(Equal(1))

	ni3 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni3.Id] = &ni3
	Ω(len(b.RegularNeurons())).Should(Equal(1))

	ni4 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[ni4.Id] = &ni4
	Ω(len(b.RegularNeurons())).Should(Equal(2))

	ni5 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[ni5.Id] = &ni5
	Ω(len(b.RegularNeurons())).Should(Equal(2))

	ni6 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni6.Id] = &ni6
	Ω(len(b.RegularNeurons())).Should(Equal(2))
}

func Test_Brain_Init(t *testing.T) {
	RegisterTestingT(t)

	b := NewBrain()
	ni1 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni1.Id] = &ni1
	ni2 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni2.Id] = &ni2
	ni3 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni3.Id] = &ni3
	ni4 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni4.Id] = &ni4
	ni5 := Neuron{Id: <-nextId, Role: Role_input}
	b.Neurons[ni5.Id] = &ni5

	nr1 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[nr1.Id] = &nr1
	nr2 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[nr2.Id] = &nr2
	nr3 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[nr3.Id] = &nr3
	nr4 := Neuron{Id: <-nextId, Role: Role_regular}
	b.Neurons[nr4.Id] = &nr4

	no1 := Neuron{Id: <-nextId, Role: Role_output}
	b.Neurons[no1.Id] = &no1

	input := map[string]float64{
		ni1.Id: 1.0,
		ni2.Id: 2.0,
		ni3.Id: 5.5,
		ni4.Id: 8.3,
		ni5.Id: 0.1,
	}
	b.Init(input)

	Ω(b.InputNeurons()[ni1.Id].HillockV).Should(Equal(1.0))
	Ω(b.InputNeurons()[ni2.Id].HillockV).Should(Equal(2.0))
	Ω(b.InputNeurons()[ni3.Id].HillockV).Should(Equal(5.5))
	Ω(b.InputNeurons()[ni4.Id].HillockV).Should(Equal(8.3))
	Ω(b.InputNeurons()[ni5.Id].HillockV).Should(Equal(0.1))
}

func Test_BeainStepForward(t *testing.T) {
	RegisterTestingT(t)

	b := NewBrain()
	n1 := NewNeuron(Role_input)
	n2 := NewNeuron(Role_regular)
	n3 := NewNeuron(Role_output)
	s1 := NewSynapse(n1, n2, 0.5, baseKernel())
	s2 := NewSynapse(n2, n2, 0.5, baseKernel())
	s3 := NewSynapse(n3, n2, 0.5, baseKernel())
	s4 := NewSynapse(n2, n3, 0.5, baseKernel())
	b.AddNeuron(n1)
	b.AddNeuron(n2)
	b.AddNeuron(n3)

	Ω(b.Time).Should(Equal(int64(0)))
	Ω(n2.Time).Should(Equal(int64(0)))
	Ω(s1.Time).Should(Equal(int64(0)))
	Ω(s2.Time).Should(Equal(int64(0)))
	Ω(s3.Time).Should(Equal(int64(0)))
	Ω(s4.Time).Should(Equal(int64(0)))
	Ω(n1.Time).Should(Equal(int64(0)))
	Ω(n3.Time).Should(Equal(int64(0)))
	b.StepForward()
	Ω(b.Time).Should(Equal(int64(1)))
	Ω(n2.Time).Should(Equal(int64(1)))
	Ω(s1.Time).Should(Equal(int64(1)))
	Ω(s2.Time).Should(Equal(int64(1)))
	Ω(s3.Time).Should(Equal(int64(1)))
	Ω(s4.Time).Should(Equal(int64(1)))
	Ω(n1.Time).Should(Equal(int64(1)))
	Ω(n3.Time).Should(Equal(int64(1)))

	b.StepForward()
	Ω(b.Time).Should(Equal(int64(2)))
	Ω(n2.Time).Should(Equal(int64(2)))
	Ω(s1.Time).Should(Equal(int64(2)))
	Ω(s2.Time).Should(Equal(int64(2)))
	Ω(s3.Time).Should(Equal(int64(2)))
	Ω(s4.Time).Should(Equal(int64(2)))
	Ω(n1.Time).Should(Equal(int64(2)))
	Ω(n3.Time).Should(Equal(int64(2)))

	b.StepForward()
	b.StepForward()
	b.StepForward()
	b.StepForward()
	b.StepForward()
	b.StepForward()
	b.StepForward()
	b.StepForward()
	Ω(b.Time).Should(Equal(int64(10)))
	Ω(n2.Time).Should(Equal(int64(10)))
	Ω(s1.Time).Should(Equal(int64(10)))
	Ω(s2.Time).Should(Equal(int64(10)))
	Ω(s3.Time).Should(Equal(int64(10)))
	Ω(s4.Time).Should(Equal(int64(10)))
	Ω(n1.Time).Should(Equal(int64(10)))
	Ω(n3.Time).Should(Equal(int64(10)))

	b.StepForward()
	Ω(b.Time).Should(Equal(int64(11)))
	Ω(n2.Time).Should(Equal(int64(11)))
	Ω(s1.Time).Should(Equal(int64(11)))
	Ω(s2.Time).Should(Equal(int64(11)))
	Ω(s3.Time).Should(Equal(int64(11)))
	Ω(s4.Time).Should(Equal(int64(11)))
	Ω(n1.Time).Should(Equal(int64(11)))
	Ω(n3.Time).Should(Equal(int64(11)))
}
