import base64

def decode16(f_bytes):
	for i in range(0,5):
		f_bytes = base64.b16decode(f_bytes)
	return f_bytes

def decode32(f_bytes):
	for i in range(0,5):
		f_bytes = base64.b32decode(f_bytes)
	return f_bytes

def decode64(f_bytes):
	for i in range(0,5):
		f_bytes = base64.b64decode(f_bytes)
	return f_bytes

# Open THM's file
f = open('encodedflag.txt', 'r')
f_bytes = f.read()

# Decode in reverse order of encoding
f_bytes = decode16(f_bytes)
f_bytes = decode32(f_bytes)
f_bytes = decode64(f_bytes)

# Print flag
print(f_bytes)