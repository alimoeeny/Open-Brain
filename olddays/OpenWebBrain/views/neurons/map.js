function(doc){
    if (doc.type=="neuron"){
        emit ([doc._id], doc)
        }
    
}
