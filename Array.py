def zigzag(n):
    indexorder = sorted(((x,y) for x in range(n) for y in range(n)),
                    key = lambda (x,y): (x+y, -y if (x+y) % 2 else y) )
    return {index: n for n,index in enumerate(indexorder)}

def printzz(myarray):
    n = int(len(myarray)** 0.5 +0.5)
    for x in range(n):
        for y in range(n):
                print "%2i" % myarray[(x,y)],
        print

number = int(raw_input("Enter number : "))
print("Zig-Zag Matrix : ")
printzz(zigzag(number))
def rot_right(a):
    return zip(*a[::-1])

def sp(m, n, start = 1):
    #Generate number range spiral of dimensions m x n 
    if n == 0:
        yield ()
    else:
        yield tuple(range(start, m + start))
        for row in rot_right(list(sp(n - 1, m, m + start))):
            yield row

def spiral(m):
    return sp(m, m)

number = int(raw_input("Enter no. for spiral pattern : "))

print "Spiral Matrix : "
for row in spiral(number):
    print(''.join('%3i' % i for i in row))

print("Enter the value of row : ")
x=int(raw_input())

print("Enter the value of column : ")
y=int(raw_input())

a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]

print
print "Enter elements of first matrix : "
for i in range(x):
         for j in range(y):
             a[i][j]=int(raw_input())

print
print "Enter the elements of second matrix : "
for i in range(x):
         for j in range(y):
             b[i][j]=int(raw_input())

print
print "Elements of First matrix is : " 
for row in a:
     print(row)

print
print "Elements of Second matrix is :" 
for row in b:
     print(row)

# Using list comprehension
result = [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

print
#print the Subtraction of 2 matrix
print "Subtraction is : "
for r in result:
   print(r)

print("Enter the value of row : ")
x=int(raw_input())

print("Enter the value of column : ")
y=int(raw_input())

a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]
 
print "Enter elements of first matrix : "
for i in range(x):
         for j in range(y):
             a[i][j]=int(raw_input())

print "Enter the elements of second matrix : "
for i in range(x):
         for j in range(y):
             b[i][j]=int(raw_input())

print
print "Elements of First matrix is : " 
for row in a:
     print(row)

print
print "Elements of Second matrix is :" 
for row in b:
     print(row)

# iterate through rows
for i in range(len(a)):
   # iterate through columns
   for j in range(len(a[0])):
       result[i][j] = a[i][j] - b[i][j]
       
print
#print the Subtraction of 2 matrix
print "Subtraction is : "
for r in result:
   print(r)

print("Enter the value of row and column of first matrix : ")
x=int(raw_input())
y=int(raw_input())
a,b = x,y

X = [x[:] for x in [[0]*y]*x]

print "Enter elements of first matrix : "
for i in range(a):
    for j in range(b):
        X[i][j]=int(raw_input())

print
print "Enter the value of row and column of second matrix : "
c=int(raw_input())
d=int(raw_input())
m,n = c,d

Y = [c[:] for c in [[0]*d]*c]


print "Enter elements of second matrix : "
for i in range(m):
    for j in range(n):
        Y[i][j]=int(raw_input())

print
print "Elements of First matrix is : "
for row in X:
    print row


print 
print "Elements of Second matrix is :"
for row in Y:
    print row

#using list comprehension
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

print
print "Matrix Multiplication : "
for r in result:
   print(r)

print("Enter the value of row and column of first matrix : ")
x=int(raw_input())
y=int(raw_input())
a,b = x,y

X = [x[:] for x in [[0]*y]*x]

print "Enter elements of first matrix : "
for i in range(a):
    for j in range(b):
        X[i][j]=int(raw_input())

print
print "Enter the value of row and column of second matrix : "
c=int(raw_input())
d=int(raw_input())
m,n = c,d

Y = [c[:] for c in [[0]*d]*c]


print "Enter elements of second matrix : "
for i in range(m):
    for j in range(n):
        Y[i][j]=int(raw_input())

print
print "Elements of First matrix is : "
for row in X:
    print row


print 
print "Elements of Second matrix is :"
for row in Y:
    print row
   
result = [[0 for row in range(0,a)] for col in range(0,n)]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

print
print "Matrix Multiplication : "
for r in result:
   print(r)


array = list()
num = raw_input("Enter number of elements : ")

print
print 'Enter '+str(num) +' numbers in array : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    array.append(int(n))
    
print
print "Numbers are : "
print array

print
find = int(raw_input("Enter Number to find closest value : "))

print

#using lambda function
takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))

print "Closest Value is : ",takeClosest(find,array)


closest = 0

array = list()
num = raw_input("Enter number of elements : ")

print
print 'Enter '+str(num) +' numbers in array : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    array.append(int(n))
    
print
print "Numbers are : "
print array

print
find = int(raw_input("Enter Number to find closest value : "))

distance = abs(closest - find)

for i in range(1,len(array)):
  distanceI = abs(array[i] - find)
  if distance > distanceI:
    closest = array[i]
    distance = distanceI

print
print "Closest Value is : ",closest



#Creating an array
array = []

#Inserting values in the Array 
array.append(1)
array.append(3)
array.append(5)

print("Elements of an Array : "+str(array))

#Changing the value of array[0]
array[0] = 2
print("Elements of an Array after changes : "+str(array))

print ("First Element of an Array : "+str(array[0]))


print("Enter the value of row : ")
x=int(raw_input())

print("Enter the value of column : ")
y=int(raw_input())

a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]
 
print "Enter elements of first matrix : "
for i in range(x):
         for j in range(y):
             a[i][j]=int(raw_input())

print "Enter the elements of second matrix : "
for i in range(x):
         for j in range(y):
             b[i][j]=int(raw_input())

print
print "Elements of First matrix is : " 
for row in a:
     print(row)

print
print "Elements of Second matrix is :" 
for row in b:
     print(row)

# Using list comprehension
result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

print
#print the Sum of 2 matrix
print "Sum of the two matrices is : "
for r in result:
   print(r)


print("Enter the value of row : ")
x=int(raw_input())

print("Enter the value of column : ")
y=int(raw_input())

a=[[0 for row in range(0,x)] for col in range(0,y)]
b=[[0 for row in range(0,x)] for col in range(0,y)]
result = [[0 for row in range(0,x)] for col in range(0,y)]
 
print "Enter elements of first matrix : "
for i in range(x):
         for j in range(y):
             a[i][j]=int(raw_input())

print "Enter the elements of second matrix : "
for i in range(x):
         for j in range(y):
             b[i][j]=int(raw_input())

print
print "Elements of First matrix is : " 
for row in a:
     print(row)

print
print "Elements of Second matrix is :" 
for row in b:
     print(row)

# iterate through rows
for i in range(len(a)):
   # iterate through columns
   for j in range(len(a[0])):
       result[i][j] = a[i][j] + b[i][j]
       
print
#print the Sum of 2 matrix
print "Sum of the two matrices is : "
for r in result:
   print(r)