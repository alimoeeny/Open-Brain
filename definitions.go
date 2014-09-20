package main

type Thing struct {
	Time int64 // the unit of this time is 100 microseconds, zero is the initialization time
}

type Brain struct {
	Thing
	Id       string
	Status   BrainStatus
	Neurons  map[string]*Neuron
	Synapses map[string]*Synapse
}

type Neuron struct {
	Thing
	Id              string
	Role            NeuronRole          // can be either input, output, or the default which is Regular (not input or output)
	Synapses        map[string]*Synapse // this includes both synapses to and from this neuron
	HillockV        float64             // to membrance potential (in millivoltes like the real thing, usual range -100mV to +50mV) of the axon Hollock of this neuron at time Time
	Recording       bool                // if true at each step the hillockv value is appenede to the holoockvhistory
	HillockVHistory []float64           // an array storing all HillockV s at each step of the Time, this will only be populated if the Reconding is on
}

type Synapse struct {
	Thing
	Id       string
	Source   *Neuron
	Target   *Neuron
	Strength float64 // the effectiveness (correlated with the number of vesicles that can be released, the excitability of the vesicles, availability of channels, and Ca++, width of the cleft, ... ) ranging from 0 to 1 . Strength cannot be negative, inhibition will be achived by negative kernels (?)
	//	Output      float64 // in it's simplest form, it is either zero (synapse is down) or one (synapse is releasing transpitters with maximum capacity, at time Time (calculated for each step based on kernel and strength
	Kernel      *Kernel // the kernel to look up the output from
	KernelIndex int     // the poision (offset) on the kernel at time Time
}

/////////// Kernels

type Kernel []float64

/////////// ENUMS

type NeuronRole string

const (
	Role_input   = "input"
	Role_output  = "output"
	Role_regular = "regular"
)

type BrainStatus string

const (
	BrainStatus_starting = "starting"
	BrainStatus_running  = "awake"
	BreainStatus_stopped = "stopped"
)
