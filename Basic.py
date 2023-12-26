y = 1
if y==1:
    print 'y is equal to 1'
x = 2
if x==1:
    print 'x is equal to 1'
else:
    print 'x is not equal to 1'
z = 3
if z==1:
    print 'z is equal to 1'
elif z==2:
    print 'z is equal to 2'
elif z==3:
    print 'z is equal to 3'
else:
    print 'z is not equal to 1 or 2 or 3'
a = 20;
b = 10;

if(a == b):
   print "a is equal to b";
else:
   print "a is not equal to b";

if(a != b ):
   print "a is not equal to b";
else:
   print "a is equal to b";

if(a <> b):
   print "a is not equal to b";
else:
   print "a is equal to b";

if(a < b):
   print "a is less than b";
else:
   print "a is not less than b";

if(a > b):
   print "a is greater than b";
else:
   print "a is not greater than b";

a = 10;
b = 20;
if(a <= b):
   print "a is either less than or equal to b";
else:
   print "a is neither less than nor equal to b";

if(b >= a):
   print "b is either greater than or equal to b";
else:
   print "b is neither greater than nor equal to b";class Employee:
   empCount = 0;

   def __init__(self, name, salary):
      self.name = name;
      self.salary = salary;
      Employee.empCount += 1;
   
   def displayCount(self):
     print "\nTotal Employee %d", Employee.empCount;

   def displayEmployee(self):
      print "\nName: ", self.name, ",Salary: ", self.salary;

emp1 = Employee("ABC", 2000);
emp2 = Employee("XYZ", 5000);
emp1.displayEmployee();
emp2.displayEmployee();
print "\nTotal Employee: ",Employee.empCount;a = 60;
b = 13;

c = a & b;       
print "Value of c: ",c;

c = a | b;        
print "Value of c: ",c;

c = a ^ b;        
print "Value of c: ",c;

c = ~a;          
print "Value of c: ",c;

c = a << 2;      
print "Value of c: ",c;

c = a >> 2;      
print "Value of c: ",c;a = 2;
b = 1;
c = 0;

c += a;
print "Value of c: ",c; 

c *= a;
print "Value of c: ",c; 

c /= a; 
print "Value of c: ",c; 

c = 1;
c %= a;
print "Value of c: ",c;

c **= a;
print "Value of c: ",c;

c //= a;
print "Value of c: ",c;a = 20;
b = 10;

c = a + b;
print "Addition Value: ",c;

c = a - b;
print "Subtraction: ",c; 

c = a * b;
print "Multiplication Value: ",c;

c = a / b;
print "Division Value: ",c;

c = a % b;
print "Mod Value: ",c;

a = 2;
b = 3;
c = a**b; 
print "Exponent Value: ",c;

a = 9;
b = 4;
c = a//b;
print "Floor Division Value: ",c;print("Enter the numbers separated by space : ")
try: raw_input
except: raw_input = input

#splitting the numbers by space and passing it to the sum function 
print("Sum of the Numbers is : " + str(sum(int(x) for x in raw_input().split())))