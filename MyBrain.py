#!/usr/bin/env python

import sys
from openbrain import *
import pylab

try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

class MyBrain:
	def __init__(self):
			
		#Set the Glade file
		self.gladefile = "MyBrain.glade"  
		self.wTree = gtk.glade.XML(self.gladefile, "mainWindow") 

		#Create our dictionay and connect it
		dic = {"on_mainWindow_destroy" : gtk.main_quit,
				"on_AddWine" : self.OnAddWine,
				"exptViewSelectionChange": self.showExperimentProperties}
		self.wTree.signal_autoconnect(dic)
		
		#Get the treeView from the widget Tree
		self.exptView = self.wTree.get_widget("exptView")
		#Add all of the List Columns to the exptView
		self.AddexptListColumn("Name", 0)
		self.AddexptListColumn("Type", 1)
		self.AddexptListColumn("Stim", 2)
		self.AddexptListColumn("Monkey", 3)
		self.AddexptListColumn("id", 4)	
		#Create the listStore Model to use with the exptView
		self.exptList = gtk.ListStore(str, str, str, str, str)
		#Attache the model to the treeView
		self.exptView.set_model(self.exptList)	
		
		self.LoadExperimentsList()
		self.exptSelection = self.exptView.get_selection()
		self.exptSelection.set_mode(gtk.SELECTION_MULTIPLE)		


	def showExperimentProperties(self, a, b):
		sel = self.exptSelection.get_selected_rows()
		print self.exptSelection.count_selected_rows().__str__() + " rows selected" 
		selectedExperimentIds = []		
		for it in sel[1]:
			selectedExperimentIds.append(sel[0][it][4])			
			#print sel[0][it][4] 
		BX = []
		for bx in selectedExperimentIds:
			Brain.Experiments[int(bx)].loadData()		
			BX.append(Brain.Experiments[int(bx)])
		experimentProperties = self.getExperimentProperties(BX)		
		print experimentProperties

	def getExperimentProperties(self, experiments):
		expProperties = []		
		for ex in experiments:
			for ep in dir(ex):
				if ep[0] != '_' and not(ep in expProperties) :
					expProperties.append(ep)
		return expProperties

	def LoadExperimentsList(self):
		for expt in Brain.Experiments:
			self.exptList.append([expt.name[3:9], expt.name.split('.')[2], expt.name.split('.')[3], expt.monkeyName, Brain.Experiments.index(expt)])		

	def AddexptListColumn(self, title, columnId):
		column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
		column.set_resizable(True)		
		column.set_sort_column_id(columnId)
		self.exptView.append_column(column)
		
	def OnAddWine(self, widget):
		"""Called when the use wants to add a wine"""
		#Cteate the dialog, show it, and store the results
		wineDlg = wineDialog();		
		result,newWine = wineDlg.run()
		
		if (result == gtk.RESPONSE_OK):
			"""The user clicked Ok, so let's add this
			wine to the wine list"""
			self.exptList.append(newWine.getList())
				
class wineDialog:
	"""This class is used to show wineDlg"""
	
	def __init__(self, wine="", winery="", grape="", year=""):
	
		#setup the glade file
		self.gladefile = "pywine.glade"
		#setup the wine that we will return
		self.wine = Wine(wine,winery,grape,year)
		
	def run(self):
		"""This function will show the wineDlg"""	
		
		#load the dialog from the glade file	  
		self.wTree = gtk.glade.XML(self.gladefile, "wineDlg") 
		#Get the actual dialog widget
		self.dlg = self.wTree.get_widget("wineDlg")
		#Get all of the Entry Widgets and set their text
		self.enWine = self.wTree.get_widget("enWine")
		self.enWine.set_text(self.wine.wine)
		self.enWinery = self.wTree.get_widget("enWinery")
		self.enWinery.set_text(self.wine.winery)
		self.enGrape = self.wTree.get_widget("enGrape")
		self.enGrape.set_text(self.wine.grape)
		self.enYear = self.wTree.get_widget("enYear")
		self.enYear.set_text(self.wine.year)	
	
		#run the dialog and store the response		
		self.result = self.dlg.run()
		#get the value of the entry fields
		self.wine.wine = self.enWine.get_text()
		self.wine.winery = self.enWinery.get_text()
		self.wine.grape = self.enGrape.get_text()
		self.wine.year = self.enYear.get_text()
		
		#we are done with the dialog, destory it
		self.dlg.destroy()
		
		#return the result and the wine
		return self.result,self.wine
		

if __name__ == "__main__":
	Brain = OpenBrain()
	wine = MyBrain()
	gtk.main()
