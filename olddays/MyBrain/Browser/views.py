from django.http import HttpResponse
import sys
sys.path.append('../')
from openbrain import OpenBrain
from PlotPSTH import PlotPSTH
from django.shortcuts import render_to_response
from django.http import Http404
from PlotRaster import PlotRaster
from numpy import squeeze

Brain = OpenBrain(dataPath='../', spikeDataPath='../data/dae/')

def index(request):
	s = []
	for ex in Brain.Experiments:
		s.append(ex.name)
	return render_to_response('Browser/index.html', {'expts_list': s})

def exptdetails(request, expt_id):
	Brain.Experiments[int(expt_id)].loadData()	
	s = []
	for dt in dir(Brain.Experiments[int(expt_id)]):
		if dt[0] != '_' : #and not(ep in expProperties) :
			s.append([dt, squeeze(eval('Brain.Experiments['+expt_id+'].' + dt)).__str__()[0:99]])
	return render_to_response('Browser/experiment.html', {'expt_prop_list': s})

def psthplot(request, expt_id):
  	#try:
	Brain.Experiments[int(expt_id)].loadData()
	response = HttpResponse(mimetype="image/png")
	PlotPSTH([Brain.Experiments[int(expt_id)]], Start=0, Finish=2000, SmoothWinLength=10, NormalizeResponses=0, CategorizeBy=None, filename = response)
	return response
	#except :
	#        raise Http404

def rasterplot(request, expt_id):
	#return HttpResponse("rasterplot goes here")
	#try:
	Brain.Experiments[int(expt_id)].loadData()
	response = HttpResponse(mimetype="image/png")
	PlotRaster([Brain.Experiments[int(expt_id)]], Start=0, Finish=2000, CategorizeBy=None, filename = response)
	return response
	#except :
	#        raise Http404

def histogram(request, expt_id, prop):
	
	return HttpResponse("a histogram goes here!")
