// Recursively lists the files in a user-specified directory.
// Open a file on the list by double clicking on it.
file_path = File.openDialog("Select a File"); //path to a single file
dir = File.getParent(file_path);
list = getFileList(dir);
   for (i=0; i<list.length; i++) {
         print(list[i]);
   }