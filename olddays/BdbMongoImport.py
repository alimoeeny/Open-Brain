from pymongo import Connection


def BdbMongoImport(Idstring):
    connection = Connection('localhost', 27017);
    db = connection.opendb;
    collection = db.things; # i need to make a collection of neurons and use that here instead as far as I understand it
    
    Expt = scipy.io.loadmat(filename, struct_as_record=True)
    Expt = Expt['Expt']
    Expt = Expt[0][0]

    ExptHeader = Expt['Header']
    ExptStimvals = Expt['Stimvals']
    ExptTrials = Expt['Trials'][0]

    print ExptTrials.size.__str__() + ' trials found. Trial range: ' + ExptTrials['Trial'][0][0][0].__str__() + ' to ' + ExptTrials['Trial'][-1][0][0].__str__()
    return Expt, ExptHeader, ExptStimvals, ExptTrials
