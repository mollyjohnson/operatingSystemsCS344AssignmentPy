#Molly Johnson
#OSU CS 344 Assignment Py
#due: 11/19/18
#ONID: johnsmol

#importing random and string, and getting a specified number of random
#lowercase chars adapted from:
#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
import random
import string

#function to get a specified number (y) of lowercase chars and join them into
#a string. Adapted from:
#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
def random_char(y):
		return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

#string length as specified in instructions
stringLength = 10

#file opening in current working directory  and writing to a file in python adapted from:
#https://www.w3schools.com/python/python_file_write.asp and
#http://www.pitt.edu/~naraehan/python3/file_path_cwd.html

#initialize string var of length 10 with the random chars from the raandom_char function
file1String = random_char(stringLength)
#concat a newline onto the string
file1String = file1String + "\n"
#use w to write to that file
file1 = open("file1.txt", "w")
#write string to the file
file1.write(file1String)
#close the file
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
