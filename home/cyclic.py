

def cyclicAttack(n,e,c):
	c0 = c
	li = []
	c1 = None
	#file = open("output.txt","a")
	while ( c1 != c):
		c1 = ( c0 ** e ) % n
		if c1 in li:
			return -1
		li.append(c1)
		print(c1)
		#file.write(str(c1) + "\n")
		prev = c0
		c0 = c1
		#c1 = None
	file.write("Final "+str(prev) + "\n")		
	file.close()
	return prev





ciphertext = int(input("Enter the Ciphertext\n"))
n = int(input("Enter the value of N\n"))
e = int(input("Enter the value of e\n"))
#e = 11
file = open("output.txt","a")
file.write("N = "+str(n) + " e= " + str(e) + " Ciphertext = "+str(ciphertext)+"\n")
file.close()
#converting to ascii
# listOfAscii = []

# for i in ciphertext:
# 	listOfAscii.append(ord(i))

# print(listOfAscii)

# PlainText = []

# for i in listOfAscii:
# 	print("Solving",i)
# 	PlainText.append(chr(cyclicAttack(int(n),int(e),int(i))))
print("Intermediate blocks")
plaintext = cyclicAttack(int(n),int(e),int(ciphertext))
print("Plain text: ",plaintext)
print("Verification")
verification = (plaintext**e)%n
print("Ciphertext",verification)
if verification == ciphertext:
	print("Verification successful")
else:
	print("Verification failed")
#print(PlainText)
#print(hack_RSA(7,143))
#print(cyclicAttack(143,3,74))