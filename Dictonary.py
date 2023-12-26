para="Hi welcome to python dictionary example"

#Initialising dictionary
chrCount={}

#getting each character from the variable para
for i in para:
 #strip fuction will remove the pre and post spaces from a string variable
 if i.strip() == "":
  continue
 # if key already exist in dictionary chrCount. add 1 to the value of the element
 if(i in chrCount):
  chrCount[i]=chrCount[i]+1
 # newly adding an key with value as 1 into the dictionary chrCount
 else:
  chrCount[i]=1

print chrCount







# empty dictionary
d = {}
d['dog'] = 1
d['cat'] = 2

# iterating over (key, value) pairs
for key, value in d.iteritems():
  print key, value
  
# dictionaries from tuple list
d1 = dict([('tiger', 1), ('lion', 2)])
d2 = dict(zip(['dog', 'cat'], [1, 2]))

# iterating over keys
for key in d1:
  print key, d1[key]

# dictionaries with two keys
d1 = {'dog': 1, 'cat': 2}
d2 = dict(wolf=1, snake=2)

# iterating over keys
for key in d2:
  print key, d2[key]






myDict = { "hello": 13,
         "world": 31,
         "!" : 71 }

#Access Dictionary elements 

# iterating over key-value pairs:
for key, value in myDict.items():
 print ("key = %s, value = %s" % (key, value))

# iterating over keys:
for key in myDict:
 print ("key = %s" % key)
    
# (is a shortcut for:)
for key in myDict.keys():
 print ("key = %s" % key)

# iterating over values:
for value in myDict.values():
 print ("value = %s" % value)