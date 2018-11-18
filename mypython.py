#Molly Johnson
#OSU CS 344 Assignment Py
#due: 11/19/18
#ONID: johnsmol

import random
import string

stringLength = 10
def random_char(y):
		return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

file1String = random_char(stringLength)
file1String = file1String + "\n"
file1 = open("file1.txt", "w")
file1.write(file1String)
file1.close()

file2String = random_char(stringLength)
file2String = file2String + "\n"
file2 = open("file2.txt", "w")
file2.write(file2String)
file2.close()

file3String = random_char(stringLength)
file3String = file3String + "\n"
file3 = open("file3.txt", "w")
file3.write(file3String)
file3.close()
