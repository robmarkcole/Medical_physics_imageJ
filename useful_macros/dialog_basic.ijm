	Dialog.create("Macro Opened");
	Dialog.addMessage("---- Some Analysis ----");
	if(nImages==0) {
		Dialog.addMessage("You will be prompted to open the required image after clicking OK");
	}
	Dialog.addMessage("open image is " + getInfo("image.filename"));
	Dialog.show()
