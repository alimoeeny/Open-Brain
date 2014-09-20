(defrecord [id name]) ; ExperimentTypes #{:DID :BDID :ABD :PassiveFixation})
(defrecord Subject [id name])
(defrecord Neuron [id name subject])
(defrecord SpikeTrain [id trial neuron spikes])
(defrecord Trial [id experiment start end properties])
(defrecord Experiment [id name experimenttype experimenter experimentdate insertdate ])
(defrecord Experimenter [id name])

