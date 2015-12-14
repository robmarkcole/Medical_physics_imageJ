// Script to query dicom header info and place in table
// Tags found by Image> Show info
requires("1.41g");  // for data table


// Navigate to file/folder ///////////////////////////////
file_path = File.openDialog("Select a File"); //path to a single file
file_name = File.getName(file_path);
directory = File.getParent(file_path);
file_list = getFileList(directory);


// create table
data_table = "Data Table";
table_pointer = "["+data_table+"]";
if (isOpen(data_table))
   print(table_pointer, "\\Clear");
else
   run("Table...", "name="+table_pointer+" width=600 height=600");
print(table_pointer, "\\Headings: File \t Image time \t Modality"); // add headings


// Loop through all files
for (i=0; i<file_list.length; i++) {
	open(directory + File.separator + file_list[i]); // open the file

	// Get DICOM info - put headings in table above
	file				= getTitle();
	Image_time 			= getInfo("0008,0033");
	Modality 			= getInfo("0008,0060");

	print(table_pointer, file + "\t" + Image_time + "\t" + Modality);
	close(); // close open image
  }






