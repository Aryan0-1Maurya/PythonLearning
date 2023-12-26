number = 0
while (number < 9):
    print 'The number is:', number
    number = number + 1

print "Good bye!"


for i in range(0,2):    
    for i in range(0,4):    
        print 'Number is %d' % (i)
    
print 'Good Bye :)'



for letter in 'Computer':
   print 'Current Letter :', letter

print "Good bye!"



d = {3: "Earth", 1: "Mercury", 4: "Mars", 2: "Venus"}

#for each loop
for k in sorted(d):
    print("%i: %s" % (k, d[k]))

print

d = {"London": "United Kingdom", "Berlin": "Germany", "Rome": "Italy", "Paris": "France"}

#for each loop
for k in sorted(d):
    print("%s: %s" % (k, d[k]))


