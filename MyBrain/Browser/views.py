from django.http import HttpResponse
import sys
sys.path.append('../')
from openbrain import OpenBrain

Brain = OpenBrain(dataPath='../')

def index(request):
	s = []
	for ex in Brain.Experiments:
		s.append(ex.name)
	return HttpResponse("Hello there, at last!" + s.__str__()) 
