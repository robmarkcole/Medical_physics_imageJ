from ij import IJ
from ij.gui import OvalRoi
from ij.plugin.frame import RoiManager
from ij.plugin.filter import Analyzer
from ij.measure import Measurements, ResultsTable

imp = IJ.getImage()  
rm = RoiManager()  # instantiate manager # throws exception if it doesn't exist
#rm = RoiManager.getInstance() # if manager exists 
 
bright_roi = OvalRoi(118,94,12,12); # define and add ROI
imp.setRoi(bright_roi)  # make active on image
rm.addRoi(bright_roi)  # add
#rm.select(0) # select the ROI

dark_roi = OvalRoi(138,144,12,12)
imp.setRoi(dark_roi)  # make active on image
rm.addRoi(dark_roi)  # add

rm.runCommand(imp,"Measure")		# this will create a new results table
rm.runCommand(imp,"Show All")		# show all ROI
rt = Analyzer.getResultsTable()		

bright_mean = rt.getValueAsDouble(rt.getColumnIndex("Max"),0)
dark_mean = rt.getValueAsDouble(rt.getColumnIndex("Mean"),1)
print "Bright :" + str(bright_mean) + " Dark: " + str(dark_mean) +  "the contrast value is :" + str(bright_mean/dark_mean) #access table by col and row