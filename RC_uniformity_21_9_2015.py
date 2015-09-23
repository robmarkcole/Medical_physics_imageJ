# follow http://imagej.net//macros/python/Image_Properties.py
# ImagePlus class contains info about the image, eg width. Process contains pixel array
from ij import IJ
from ij.plugin import Duplicator
from ij.io import OpenDialog 
######### Helper functions
def getUniformity(min, max):
	return 100.0*((max - min)/(max + min))

######### open image using dialogue box
#imp = IJ.getImage()   
od = OpenDialog("Choose image file", None)  
filename = od.getFileName()  
directory = od.getDirectory()  
filepath = directory + filename  
#print filepath
original = IJ.openImage(filepath)
original.show()

########## Use thresholding and selection to define UFOV
IJ.setRawThreshold(original, 1, 255,'')  # background pixels have value 0
IJ.run(original, "Create Selection", "")   # add bounding box
IJ.run(original,"To Bounding Box", "")    # this box defines the UFOV
IJ.resetThreshold(original)		# get back original now UFOV is definedthresholding

UFOV = Duplicator().run(original) # duplicate the original image, only the CFOV
UFOV.setTitle("UFOV")
UFOV.show() 

CFOV_fraction = 0.75  # choose the fraction of the UFOV that defines the CFOV
IJ.run(original,"Scale... ", "x="+str(CFOV_fraction)+" y="+str(CFOV_fraction)+" centered") # rescale bounding box to get CFOV

CFOV = Duplicator().run(original) # duplicate the original image, only the CFOV
CFOV.setTitle("CFOV")
CFOV.show() 

######### Nema process including Re-bin image to larger pixels
desired_pixel_width = 6.4 # ENTER mm, remember tolerance is +/-30%
current_pixel_width =  CFOV.getCalibration().pixelWidth  #get pixel width, 1.16 mm
shrink_factor = int(desired_pixel_width/current_pixel_width)  # must be an integer

IJ.run(CFOV, "Bin...", "x="+str(shrink_factor)+" y="+str(shrink_factor)+" bin=Sum") # run the bin plugin
IJ.run(CFOV, "Convolve...", "text1=[1 2 1\n2 4 2\n1 2 1\n] normalize")  # apply the nema filter

######## Analyse pixels
CFOVpixels = CFOV.getProcessor().convertToFloat().getPixels()     # access processor, get float array of pixels

CFOVmean = sum(CFOVpixels) / len(CFOVpixels) 
#pixels_above_threshold = filter(lambda pix: pix > 0.75*mean, pixels)  # return a new array with values above zero, use anonymous function

CFOVunifiormity = getUniformity(min(CFOVpixels), max(CFOVpixels))
IJ.log("The integral uniformity of the CFOV is: " +str(CFOVunifiormity) + "%")
