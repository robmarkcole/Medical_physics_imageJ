// Script to query dicom header info, files must be .dcm
// Tags found by Image> Show info

//open("C:\\Users\\RCole02\\Desktop\\Research\\imageJ\\Ultrasound image edge detection for Pedrum\\US images - subset\\IM_0001.dcm");  // if no file opened then operates on current image
studyID 			= getInfo("0020,0010");
studyModality 		= getInfo("0008,0060");
print("Study ID: "+ studyID);
print("Study ID: "+ studyModality);
