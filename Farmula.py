from fractions import *

a = Fraction(raw_input("Enter first fraction number : "))

print

b = Fraction(raw_input("Enter second fraction number : "))

print
print "Addition of",a,"and",b,"is :",(a+b)



#take user input
F = float(raw_input('Enter temperature in Fahrenheit : '))

#convert fahrenheit to celsius
C = ((5.0/9.0)*(F - 32))

print
print "Temperature in degree Celsius is %f" %C



def factorial(num):
 if num==1:
  return 1
 else:
  return num * factorial(num-1)

num = input("Enter number: ");
fact = factorial(num);
print "\nFactorial of",num,"is:",fact;



def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       binary(n//2)
   print n%2,

# Take decimal number from user
dec = int(input("Enter a number : "))

print
print "The binary representation of ",dec," is ",
binary(dec)




# Take decimal number from user
dec = int(input("Enter a number : "))

#convert decimal to binary
bin(dec)
          
#convert decimal to octal
oct(dec)

#convert decimal to hexadecimal
hex(dec)

print
print "The decimal value",dec,": "
print "In binary is :",format(dec, 'b')
print "In octal is :",format(dec, 'o')
print "In hexadecimal is :",format(dec, 'x')




# take input from the user in degree celsius
celsius = float(input('Enter degree Celsius : '))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))




binary = raw_input('Enter Binary no. to convert in Decimal : ')

print

print "The Decimal Representation of ",binary," is ",int(binary, 2)




from collections import Counter
def modes(values):
 count = Counter(values)
 best = max(count.values())
 return [k for k,v in count.items() if v == best]

num_array = list()

num = raw_input("Enter how many elements you want: ")

print 'Enter numbers : '
for i in range(int(num)):
        n = raw_input("num"+str(i+1)+": ")
        num_array.append(int(n))
    
print "Arithmetic Mode : " +str(modes(num_array))




from collections import defaultdict
def modes(values):
 count = defaultdict(int)
 for v in values:
  count[v] +=1
 best = max(count.values())
 return ([k for k,v in count.items() if v == best])

num_array = list()

num = raw_input("Enter how many elements you want: ")

print 'Enter numbers : '
for i in range(int(num)):
        n = raw_input("num"+str(i+1)+": ")
        num_array.append(int(n))
    
print "Arithmetic Mode : " +str(modes(num_array))





def median(aray):
    srtd = sorted(aray)
    print "Elements in sorted order : "+str(srtd)
    alen = len(srtd)
    return 0.5*( srtd[(alen-1)//2] + srtd[alen//2])

num_array = list()
num = raw_input("Enter how many elements you want: ")
print 'Enter numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(float(n))
print "Arithmetic Median : "+str(median(num_array))




def avg(data):
    if len(data)==0:
        return 0
    else:
        return sum(data)/float(len(data))
    
num_array = list()
num = raw_input("Enter how many elements you want: ")
print 'Enter numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+": ")
    num_array.append(int(n))
print "Arithmetic Mean : "+str(avg(num_array))




# Three sides of the triangle a, b and c are provided by the user

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)




# Three sides of the triangle a, b and c are provided by the user

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)




# Area of Triangle (1/2 * base * height)

def areaoftriangle( base, height ):
    area = 0.5 * base * height
    return area

base = float(raw_input("Enter base of the triangle : "))
height = float(raw_input("Enter height of the triangle : "))

print 'The area of the triangle is %0.2f' %areaoftriangle( base, height )




#Area of a square is side * side where side is sides of square.
def areaofsquare(side):
    return side * side;

side = int(raw_input("Enter value of the sides of square : "))
print "Area of square : ",areaofsquare(side)




#Area of a rectangle = length * width.
def areaofrectangle(l,w):
    return l * w;

length = int(raw_input("Enter the length of Rectangle : "))
width = int(raw_input("Enter the width of Rectangle : "))

print "Area of rectangle : ",areaofrectangle(length,width)





class Area:

 def __init__(self,radius):
  self.radius = radius;
  
 def area(self):
  a = 3.14 * radius * radius;
  print "\nArea of Circle:",a;
  
radius = input("\nEnter Radius: ");
a1 = Area(radius);
a1.area();


#Volume of Circle Example
import math
radius = float(raw_input("Enter the radius of the cylinder in cm: "))
height = float(raw_input("Enter the height of the cylinder in cm: "))

volume = math.pi*radius*radius*height

print("Volume of the Cylinder is ",volume,"cubic cm.")




# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print "The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)




import math;

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)));

def for_test(x, y):
    for y in range(x):
        return combination(x, y);

def pascals_triangle(rows):
    result = [];
    for count in range(rows):
        row = [];
        for element in range(count + 1):
            row.append(combination(count, element));
        result.append(row);
    return result;
	
num = int(raw_input("\nEnter number of rows till u want Pascal Triangle: "));
for row in pascals_triangle(num):
    print(row);




number = raw_input("Enter a octal number : ")

i = int(number,8)

print
print "The decimal representation of octal number",number,"is :",i





from fractions import *

a = Fraction(raw_input("Enter first fraction number : "))

print

b = Fraction(raw_input("Enter second fraction number : "))

print
print "Subtraction of",a,"and",b,"is :",(a-b)



number = raw_input("Enter a hexadecimal number : ")

i = int(number,16)

print
print "The decimal representation of hexadecimal number",number,"is :",i



def gcd(a,b):
 rem = a%b;
 if(rem==0):
  return b;
 else:
  return(gcd(b,rem));

a = int(raw_input("\nEnter num1: "));
b = int(raw_input("\nEnter num2: "));

result = gcd(a,b);
print "\nGCD of ",a," and ",b,": ",result;