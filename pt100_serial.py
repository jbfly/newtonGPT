maxUnsigned = 0x1FFFFFFF
bitsInUnsigned = int(29)
seventyFivePercent = int(22)
twelvePercent = int(4)
highBits = 0x1E000000
lowBits = 0x01FFFFFF

def generateRegCode(userName):
	reg = ""
	sn = ""
	
	string = userName + "PT100"

	while len(string) < 20:
		string = string + string

	h = int(0)
	g = int(0)
	s_len = len(string)

	for i in range(s_len):
		h = (((h << twelvePercent) & maxUnsigned) + ord(string[i])) & maxUnsigned
		g = h & highBits
		if g != 0:
			h = (h ^(g >> seventyFivePercent)) & lowBits

	for i in range(0, 26, 3):
		reg = reg + chr(((h>>i) & 0x0f) + 97);

	return(reg)

if __name__ == "__main__":
	name = input("Please enter the Newton's serial number\n")
	print("Registration key is:\n")
	print(generateRegCode(name))
