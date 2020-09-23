import os
import shutil #Lib to remove dirs+files
import zipfile
import exiftool

# Name of original zip file
FILENAME = "final-final-compressed.zip" 
#A dir to work with unzip files
TARGET_DIR = "unziped/"
#The tag that contains version in metadata
VERSION_TAG = "XMP:Version"

#Main function
def main():
	print("Unziping...")
	remove_dir(get_path(TARGET_DIR))
	create_dir(get_path(TARGET_DIR))
	unzip(get_path(FILENAME), get_path(TARGET_DIR))

	print("\nZIP Files:")
	print_filenames(get_path(TARGET_DIR))

	process_zip_files()

	print("\nTXT Files:")
	print_filenames(get_path(TARGET_DIR))
	totalFiles = count_files(get_path(TARGET_DIR))

	print("Files extracted: " + str(totalFiles))

	print("\nProcessing metadata...")
	process_txt_files()

	print("\nSearching for password...")
	find_file_with_password()

#Function that process the zip files from the original zip file
def process_zip_files():
	#list all unziped files
	listOfFiles = os.listdir(get_path(TARGET_DIR))
	for filename in listOfFiles:
		path = get_path(TARGET_DIR+filename)
		#Check if it is a zip file
		if (zipfile.is_zipfile(path)):
			#Unzip it and remove it
			unzip(path, get_path(TARGET_DIR))
			remove_file(path)

#Function that process the text files from the zip files and
#search for version in metadata
def process_txt_files():
	#Variable to store version count
	versionCount = 0
	listOfFiles = os.listdir(get_path(TARGET_DIR))
	for filename in listOfFiles:
		path = get_path(TARGET_DIR+filename)
		#Call function to check if it has version 1.1
		if has_metadata_version(path):
			versionCount += 1

	print("Files with Version 1.1: " + str(versionCount))

#Function to search for the word 'password' in txt files.
def find_file_with_password():
	listOfFiles = os.listdir(get_path(TARGET_DIR))
	for filename in listOfFiles:
		path = get_path(TARGET_DIR+filename)
		#Call function to read the lines of the file
		lines = read_file(path)

		#Search for password in every line
		for line in lines:
			#Call function to check if password is present
			if has_password(line):
				print("Has password: " + path)

#Function to unzip a file in a target dir
def unzip(path, target_dir):
	with zipfile.ZipFile(path, 'r') as zip_ref:
		zip_ref.extractall(target_dir)

#Function that print all files names in a dir
def print_filenames(dir):
	listOfFiles = os.listdir(dir)
	for l in listOfFiles:
		print(l)

#Function that checks a tag in metadata for version 1.1
def has_metadata_version(path):
	with exiftool.ExifTool() as et:
		tag = et.get_tag(VERSION_TAG, path)
		return tag != None

#Check if a string has the word 'password'
def has_password(line):
	return line.find('password') != -1

#Read the lines of a file
def read_file(path):
	with open(path, encoding="utf-8", errors="ignore") as reader:
		return reader.readlines()

#Count files in a dir
def count_files(dir):
	listOfFiles = os.listdir(dir)
	return len(listOfFiles)

#Return full path
def get_path(filename = None):
	path = "./"
	if (filename != None):
		path = path + filename
	return path

#Remove a dir and files in it
def remove_dir(dir):
	if os.path.exists(dir):
		shutil.rmtree(dir)

#Remove a single file
def remove_file(path):
	if os.path.exists(path):
		os.remove(path)

#Check if a dir exists and create it if not
def create_dir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)



if __name__ == "__main__":
	main()