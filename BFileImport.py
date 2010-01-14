import scipy.io

def BFileImport(filename):
    Expt = scipy.io.loadmat(filename, struct_as_record=True)
    Expt = Expt['Expt']
    Expt = Expt[0][0]

    ExptHeader = Expt['Header']
    ExptStimvals = Expt['Stimvals']
    ExptTrials = Expt['Trials'][0]

    print ExptTrials.size.__str__() + ' trials found. Trial range: ' + ExptTrials['Trial'][0][0][0].__str__() + ' to ' + ExptTrials['Trial'][-1][0][0].__str__()
    return Expt, ExptHeader, ExptStimvals, ExptTrials
