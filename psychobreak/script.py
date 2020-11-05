import os

# Wordlist filename
WL_FILENAME = "random.dic" 

#Program name
P_FILENAME = "program"

#Main function
def main():
	print("Starting...")
	#Call function to read the lines of the file
	lines = read_file(WL_FILENAME)

	#Read line by line
	for line in lines:
		ret = execute_program(line)

		#Check if the output is correct
		if is_correct(ret):
			print("Correct word: " + line)
			print("Original output: ")
			print(ret)
			return;
		else:
			print("Incorrect: " + line)

#Execute program and return its output
def execute_program(line):
	stream = os.popen('./' + P_FILENAME + ' ' + line)
	return stream.read()

#Check if a string does not have Incorrect as output
def is_correct(line):
	return not line.find('Incorrect') != -1

#Read the lines of a file (the wordlist)
def read_file(path):
	with open(path, encoding="utf-8", errors="ignore") as reader:
		return reader.readlines()


if __name__ == "__main__":
	main()