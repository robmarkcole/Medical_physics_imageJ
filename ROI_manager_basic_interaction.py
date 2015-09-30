from ij import IJ
from ij.gui import OvalRoi
from ij.plugin.frame import RoiManager

imp = IJ.getImage()  
rm = RoiManager()  # instantiate manager # throws exception if it doesn't exist
#rm = RoiManager.getInstance() # if manager exists 
 
roi = OvalRoi(75, 75, 50, 50); # define and add ROI
imp.setRoi(roi)  # make active on image
rm.addRoi(roi)  # add
rm.select(0) # select the zeroth ROI and rename it
rm.runCommand("Rename", "roi");
