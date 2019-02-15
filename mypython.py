#Molly Johnson
#OSU CS 344 Assignment Py
#due: 2/27/19
#ONID: johnsmol
#python version used: Python 3. Run with: python3 mypython.py
#Adapted from my own work previously created on 11/19/18 (I took
#the class previously in the Fall 2018 term but am retaking for a
#better grade).

#importing random and string, and getting a specified number of random
#lowercase chars adapted from:
#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
import random
import string

#function to get a specified number (y) of random lowercase chars and join them into
#a string and return this string. Adapted from:
#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
def random_char(y):
		return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

#set string length as specified in instructions
stringLength = 10

#file creating/opening in current working directory and writing to that file in python adapted from:
#https://www.w3schools.com/python/python_file_write.asp and
#http://www.pitt.edu/~naraehan/python3/file_path_cwd.html

#initialize string var of length 10 with the random chars from the random_char function
file1String = random_char(stringLength)
#concat a newline onto the string
file1String = file1String + "\n"
#open the file (using w b/c are going to create and write to that file)
file1 = open("file1.txt", "w")
#write string to the file
file1.write(file1String)
#close the file
file1.close()

#do the same for second file/second string
#initialize string var of length 10 with the random chars from the random_char function
file2String = random_char(stringLength)
#concat a newline onto the string
file2String = file2String + "\n"
#open the file (using w b/c are going to create &  write to that file)
file2 = open("file2.txt", "w")
#write string to the file
file2.write(file2String)
#close the file
file2.close()

#do the same for third file/ third string
#initialize string var of length 10 with the random chars from the random_char function
file3String = random_char(stringLength)
#concat a newline onto the string
file3String = file3String + "\n"
#open the file (using w b/c are going to create and write to that file)
file3 = open("file3.txt", "w")
#write string to the file
file3.write(file3String)
#close the file
file3.close()

#printing a string with no newline character added at the end (as would happen with print function normally) adapted from:
#https://www.w3resource.com/python-exercises/python-basic-exercise-50.php

#print from char 0 to 11, with the end being blank (i.e. no additional  newline or space added, will just print exactly what's in the file)
#(end is "" so that no additional chars are added after the 0-11 chars are printed).

#print chars 0-11 from file 1 to terminal. 
for i in range (0,11):
		print(file1String[i], end="")

#print chars 0-11 from file 2 to terminal. 
for j in range (0,11):
		print(file2String[j], end="")

#print chars 0-11 from file 3 to terminal. 
for k in range (0,11):
		print(file3String[k], end="")

#getting two random ints from a range of ints adapted from:
#https://www.geeksforgeeks.org/python-generate-random-numbers-within-a-given-range-and-store-in-a-list/

#get two random integers from 1 to 42 (inclusive) and print on separate lines

#set min and max values (inclusive) for the random ints
min = 1
max = 42

#get two random numbers in the specified range
num1 = random.randint(min, max)
num2 = random.randint(min, max) 

#print the two random numbers (using just the print function will add a newline)
print(num1)
print(num2)

#multiplying two ints in python adapted from:
#https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators

#print product of the two numbers and print on another new line
print(num1 * num2)
