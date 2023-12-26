aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)

print "The List elements are : ", aList


list1 = ['SuperMan', 'BatMan', 'The Mask'];

#Print entire list
print list1

#Print with index value
print list1[0]
print list1[1]
print list1[2]

#Delete list element
del list1[0]
print list1



#Extended Slice Syntax : arguments as [start:stop:step]
#display the elements of a list that have even indexes
L = range(10)
print "Elements of List having even indexes : ",L[::2]

print
#Display the list in reverse order
print "Elements of List in reverse order : ",L[::-1]

print
#Display substring ac from abcd
s='abcd'
print "To print substring ac from abcd : ",s[::2]

print
#Display string in reverse order
print "Reverse a string : ",s[::-1]

print
#Assignment to a regular slice can be used to change the length of the sequence
a = range(3)
print "Elements are : ",a
#Assigning new elements from index 1 to 3 as index starts from 0
a[1:3] = [4, 5, 6]
print "New List after assigning values from index 1 to 3 : ",a

print
#Deletion of elements
a = range(4)
print "Elements in the list : ",a
[0, 1, 2, 3]
print "Elements of List having even indexes : ",a[::2]
del a[::2]
print "Elements in the list after deletion : ",a

print
#Slice Example
a = range(4)
print "Elements are : ",a
print "Elements of even indexes : ",a[::2]
a[::2] = [0, -1]
print "Elements after replacing values 0 and 2 with 0 and -1 : ",a
[0, 1, -1, 3]
#a[::2] = [0,1,2] #This will give error
"""Because When assigning to an extended slice, the list on the right hand side of
the statement must contain the same number of items as the slice it is replacing
"""

print
#pass slice objects to the __getitem__ methods of the built-in sequences
#slice(start:stop:step)
print "Get Elements using getitem method : ",(range(10).__getitem__(slice(0, 5, 2)))
#Or use slice objects directly in subscripts:
print "Get Elements using slice : ",(range(10)[slice(0, 5, 2)])





list1 = ['SuperMan', 'BatMan', 'The Mask', 'SpiderMan'];

#Print entire list
print "The list is: \n", list1

#Reverse the list
list1.reverse()

#Print entire list
print "\nThe reversed list is: \n", list1

#Print the index of an object within the list
print "\nThe object 'The Mask' is at index: ", list1.index('The Mask')

#Remove object from the list
list1.remove('SpiderMan')

#Print entire list
print "\nAfter Removing SpiderMan: \n", list1