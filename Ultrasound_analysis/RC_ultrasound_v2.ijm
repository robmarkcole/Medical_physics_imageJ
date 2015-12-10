/// Some dialog to inform user ///////////////////////////////
Dialog.create("Robin Ultrasound Macro v1");
Dialog.addMessage("Navigate to the file to start analysis from");
Dialog.show()

// Navigate to file/folder ///////////////////////////////
file_path = File.openDialog("Select a File"); //path to a single file
file_name = File.getName(file_path);

directory = File.getParent(file_path);
file_list = getFileList(directory);

	for (i=0; i<file_list.length; i++) {

		// Open file and do analysis  ///////////////////////////////
		open(directory + File.separator + file_list[i]); // open the file
		makeLine(510, 23, 508, 768); // add line for profile
		//run("Plot Profile");	// plots profile - not necessary
		run("Measure"); // adds measurements to results table
		setResult("File", i, file_list[i]);  // add file name to results table

		wait(1000); //pause to inspect image
		close(); // close open image
   }

IJ.renameResults("Ultrasound analysis results"); // rename results table