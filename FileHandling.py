print "Type the filename "

filename = raw_input("> ")

print "We're going to erase %r." % filename

print "Opening the file..."

'''this will open the file if it is exist
if file does not exist it will create new file '''
target = open(filename, 'w')

'''we will truncate data of file if file is already exist'''
print "Truncating the file."
target.truncate()

print "Write three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "We are going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()




from os.path import exists

print "Type the filename :"
file= raw_input("> ")
if exists(file):
    txt_again = open(file,'r')
    print txt_again.read()
else:
    print "no such file"





#file io example
# encoding=utf-8
import io

f = io.open("text.txt", "wt", encoding="utf-8")
inputtext = raw_input("Enter text in the file : ")
f.write(unicode(inputtext))
f.close()

print
print "Contents in the file text.txt are : "
text = io.open("text.txt", encoding="utf-8").read()
print(text)




#copy content from one file to other.

import shutil

shutil.copyfile("abc.txt", "xyz.txt")

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('xyz.txt')

print "The contents of another file : "
print

while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    print line,
# close the file
f.close()