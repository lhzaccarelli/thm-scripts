import requests

#Host on port 3000
host = "http://10.10.169.100:3000/"
#Original path /
path = ""

#Variable for flag
flag = ""

print ("Running")
#Run the script while path is not equal to 'end'
while (path != "end"):
	#Get request to server
	response = requests.get(host+path)

	#Convert the response to json
	json = response.json()

	#Get value and next path
	value = json['value']
	path = json['next']

	#Check if value is different to 'end'
	if (value != "end"):
		#Copy value char to the end of flag
		flag += value

#When loop is over, print flag.
print("Flag: " + flag)