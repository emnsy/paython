import os
def rename_files():
	file_list=os.listdir(r"C:\py\prank")
	#store current directory in a var
	saved_path=os.getcwd()
	# cahnge the directory to that has the files to rename
	os.chdir(r"C:\py\prank")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
		# rechange the current directory
	os.chdir(saved_path)
rename_files()