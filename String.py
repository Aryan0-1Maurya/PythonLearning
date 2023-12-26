var1 = 'Hello World!'
var2 = "Python Programming"

#Print entire String
print var1

#Print SubString from String
print "var1[0]: ", var1[0]
print "var2[1:6]: ", var2[1:6]




var1 = "python"
var2 = "Programming"

#Capitalizing first letter of string
print 'The Capitalized String is: ', var1.capitalize()

#Getting the length of the string
print 'The length of the String is: ', len(var1)

#Converts uppercase letters in string to lowercase
print 'The String in lower case: ', var1.lower()

#Converts lowercase letters in string to uppercase
print 'The String in upper case: ', var1.upper()

#Converts lowercase letters to uppercase and vice versa
print 'The String in inverted case: ', var2.swapcase()






var1 = "this is python programming"
var2 = "this is is python"

#Title - All words begin with uppercase and the rest are lowercase
print "Title: ", var1.title()

#Counts how many times str occurs in string or in a substring
#of string if starting index beg and ending index end are given
print "Count of 'is': " , var2.count('is')

#Count 'is' between 0 to 5 range
print "Count of 'is' with range: ", var2.count('is',0,5)

#Determines if string or a substring of string (if starting 
#index beg and ending index end are given) ends with suffix; 
#returns true if so and false otherwise
print "String ends with 'python': ", var2.endswith('python')

#Determines if string or a substring of string (if starting 
#index beg and ending index end are given) starts with substring 
#str; returns true if so and false otherwise
print "String starts with 'this': ", var2.startswith('this')

#Determine if str occurs in string or in a substring of string
# if starting index beg and ending index end are given returns 
#index if found and -1 otherwise
print "Is 'python' there is var1: ", var1.find('programming')
print "Is 'python' there is var2: ", var2.find('programming')





#using raw_input
name=raw_input('Enter your name : ')
print ("Hi %s, Let us be friends!" % name);

#using only input
#remember to you double quotes ("") while giving input
place=input('\nWhere do you live? : ')
print ("I live in %s" % place);






#String Concat Example
var1 = 'Hello Harry'
var2 = var1 + ' Potter!!'
print var2

#String Replace 'Harry Potter' with 'Muggle'
print var2[:6] + 'Muggle'




def reverse(s):
    r = ""
    for c in s:
        r = c + r
    return r

string = raw_input("Enter a string to reverse : ")
print reverse(string)





s = raw_input("Enter a string to reverse : ")

#Using reversed() built-in function
print "".join(reversed(s))





string = raw_input("Enter a string to reverse : ")
#using Generator Expression
print "".join(string[c] for c in xrange(len(string) - 1, -1, -1))




string = raw_input("Enter a string to reverse : ")

#Using Extended Slice Syntax
"""If start is omitted it defaults to 0 and
if stop is omitted it defaults to the length of the string.
A step of -1 tells Python to start counting by 1 from the stop
until it reaches the start."""

print string[::-1]





# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# take input from the user
my_str = raw_input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print
print(no_punct)





var1 = 'Hello World!'
var2 = "Python Programming"

#Print entire String
print var1

#Escape character \t is used for Tab
print 'This is \t', var1
print 'This is \t\t', var2

#Print for indentation or empty line
print ''

#Escape character \n is used for Newline
print 'This is \n', var1
print 'This is \n\n', var2





# take input from the user
ip_str = raw_input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.lower()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print
print(count)





# string of vowels
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

# take input from the user
ip_str = raw_input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.lower()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

#count number of vowels
nov = sum(ip_str.count(c)for c in vowels)
#count number of consonants
noc = sum(ip_str.count(c)for c in consonants)

print
print(count)
print
print "Number of Vowels in a string : ",nov
print
print "Number of Consonants in a string : ",noc






def isAnagram(original, test):
    if len(original) == len(test):
        count = [0] * ord('z')
        for c in original:
            count[ord(c)] += 1
        for c in test:
            if count[ord(c)] == 0:
                return False
            else:
                count[ord(c)] -= 1
        return True
    return False

original = raw_input("Enter first string : ")
test = raw_input("Enter second string : ")

print
print "%s and %s are %s" % (original, test, "anagrams" if (isAnagram(original, test)) else "not anagrams")