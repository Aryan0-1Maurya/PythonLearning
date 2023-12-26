tup1 = ('harry', 'ron');
tup2 = (1, 2, 3);

#Creating a new tuple from two tuples
tup3 = tup1 + tup2
print "tup3: ", tup3

#Creating tuple by adding tuple values
tup4 = (1,2,3) + ('a','b','c')
print "tup4: ", tup4

#Print length of a tuple
print 'Length of tup4: ', len(tup4)

#Repeating a value in a tuple
tup5 = ('a',)*8
print "tup5: ", tup5

#Check value in tuple
print "Is '2' present in tup4: ", 2 in tup4

#Looping a tuple
for x in tup4: print x,





tup1 = ('harry', 'ron');
tup2 = (1, 2, 3);
tup3 = (1, 2, 3);

list1 = ['a','b','c']

#Compares elements of both tuples.
#If tup1 is greater (1), if tup1 is smaller (-1), is both are same (0)
print "Comparison of tup1 & tup2: ", cmp(tup1, tup2)
print "Comparison of tup2 & tup3: ", cmp(tup2, tup3)

#Print length of a tuple
print 'Length of tup2: ', len(tup2)

#Print item from the tuple with max value.
print 'Max of tup2: ', max(tup2)

#Print item from the tuple with min value.
print 'Min of tup2: ', min(tup2)

#Converts a list into tuple.
tup4 = tuple(list1)
print "Converted tuple from list: ", tup4





tup1 = ('harry', 'ron', 1999, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]