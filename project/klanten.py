import random
import string


thefile = open("klanten.txt", "w")
numblist = [0,1,2,3,4,5,6,7,8,9]
alfalist = list(string.ascii_lowercase)



theid = 1


numlines = int(input("how many lines? (int)    "))

for _ in range(numlines):
	totalstring = ""
	email = ""
	name = ""
	passw = ""
	
	
	for x in range(8):
		email += (random.choice(alfalist))
	email += '@'
	for x in range(5):
		email += (random.choice(alfalist))
	email += ('.com')
	for x in range(6):
		name += (random.choice(alfalist))
	for x in range(8):
		passw += (random.choice(alfalist))

	thefile.write(str(theid) + ',' + email + ',' + name + ',' + passw + '\n')

	theid += 1

thefile.close()
	
	
	

