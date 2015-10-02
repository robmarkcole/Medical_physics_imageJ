# use centre of mass to locate film, use http://imagej.net/developer/api/ij/process/ImageStatistics.html
from ij import IJ
from ij.process import ImageStatistics as IS
from ij.process import ImageProcessor
from ij.measure import Measurements as Measure

imp = IJ.openImage("C:\\Users\\RCole02\\Desktop\\images\\wrong.JPG")
imp.show()

if imp.height > imp.width:
	IJ.run(imp, "Rotate 90 Degrees Right", "")
print "image now horizontal"

ip = imp.getProcessor()

stats = IS.getStatistics(ip, Measure.CENTER_OF_MASS, imp.getCalibration()) 
print "xCenterOfMass: " + str(stats.xCenterOfMass) + "yCenterOfMass: " + str(stats.yCenterOfMass)

if stats.yCenterOfMass < 0.5*imp.height:
	IJ.run(imp, "Flip Vertically", "")