from ij import IJ
from ij.util import DicomTools

imp = IJ.getImage()   
studyDescription = DicomTools.getTag(imp, "0008,1030")
print("Study Description: "+ studyDescription)