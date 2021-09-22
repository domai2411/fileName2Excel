import os
import tkinter
from tkinter import filedialog
import pandas as pd
# import glob

def file2excel(): 
	df = pd.DataFrame(columns=['Filename'])
	script=(os.path.basename(__file__))
	root = tkinter.Tk()
	root.withdraw()
	currdir = os.getcwd()
	tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select mib directory')
	if len(tempdir) > 0:
		upa=os.path.abspath(tempdir)
		file_folder=subdirs(upa)
		# files = fileList(upa)
		# folders = folderList(upa)
		# file_folder=files+folders 
		for file in file_folder:
			if file!=script:
				print(file)
				df = df.append({'Filename': file}, ignore_index=True)
	df.head()
	df.to_excel('file2excel.xlsx')
def fileList(source):
	matches = []
	depth=1
	for root, dirnames, filenames in os.walk(source):
		if root[len(source):].count(os.sep) < depth:
				for filename in filenames:
					# if filename.endswith(('.jpg', '.MOV', '.avi', '.mpg')):
					matches.append(filename)
	return matches
def folderList(source):
	matches = []
	depth=1
	for root, dirnames, filenames in os.walk(source):
		if root[len(source):].count(os.sep) < depth:
				for dirname in dirnames:
					# if filename.endswith(('.jpg', '.MOV', '.avi', '.mpg')):
					matches.append(dirname)
					# matches.append(os.path.join(root, dirname))
	return matches
def subdirs(path):
    matches = []
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and (entry.is_dir() or entry.is_file()):
            matches.append(entry.name)
    return matches
def main():
	if os.path.exists("demofile.txt"):
		os.remove("file2excel.xlsx")
	file2excel()
	
	# currdir = os.getcwd()
	# subdirs(currdir)
	# print(fileList("."))
	# print(folderList("."))
	# os.listdir('.')
	print ("############################################")
	input("Done. Close this Window to Exit...")
	
if __name__ == "__main__":
    main()