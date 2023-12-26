import math

def perfectsquare(start,end):
    sum1 = 0
    for i in range(start,end):
        s = float(math.sqrt(i))
        n = int(math.floor(s))
        if(s == n):
            print i,
            sum1 += i
    print
    print "Sum of the perfect square numbers between the range",start,"to",end,"are : ",sum1

start = int(raw_input("Enter starting value of the range : "))
end = int(raw_input("Enter ending value of the range : "))

print
print "The Perfect Square Numbers present between the range",start,"to",end,"are :"

perfectsquare(start,end)





def perfectsquare(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1

        if ans*ans != x:  
            print x, 'is not a perfect square.'
        else:
            print x, ' is a perfect square.'
    else:
        print x, ' is not a positive number.'

number = int(raw_input("Enter a number : "))

print

perfectsquare(number)





def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
         temp = a
         a = b
         b = temp + b
    return a

# take input from the user
nterms = int(input("How many terms? "))

# Display the first 15 Fibonacci numbers.
for c in range(0, nterms):
    print (fibonacci(c)),





# define a function
def print_factors(x):
   """This function takes a
   number and prints the factors"""

   print
   print "The factors of",x,"are:"
   for i in range(1, x + 1):
       if x % i == 0:
           print i,

# take input from the user
num = int(input("Enter a number : "))

print_factors(num)




# take input from the user
num = input("Enter a number: ")

num = int(num)

factorial = 1

if num < 0:
   print "Sorry, factorial does not exist for negative numbers"
elif num == 0:
   print "The factorial of 0 is 1"
else:
   for i in range(1,num + 1):
       factorial = factorial * i

   print "The factorial of",num,"is",factorial





i = int(raw_input("Enter a Number "))

def is_even(i):
 return (i % 2) == 0
   
if is_even(i) :
 print(str(i)+" is an Even Number")
else:
 print(str(i)+" is an Odd Number ")






number = str(raw_input("Enter a number to check whether its a Duck number or not : "))

c = 0

#to check whether number contains zero or not 
for i in range(1,len(number)):
    ch = number[i]
    if ch == '0':
        c +=1

f = number[0]

print
if c > 0 and f!='0':
    print number,"is a Duck number"
else:
    print number,"is not a Duck number"




num = int(raw_input("\nEnter num: "));

print "\nPrime number: ";
for i in range(1,(num+1)):
 flag=0;
 for j in range(2,i):
  if(i%j == 0):
   flag=1;
   break;
	
 if(flag==0):
  print "\n",i;





number = int(raw_input("Enter a number to check whether its Disarium number or not : "))

c = 1
x = number
sum = 0
rev = 0

while number > 0:
    rev = rev * 10 + number % 10
    number = number / 10

while rev > 0:
    sum = sum + pow(rev % 10,c)
    c +=1
    rev = rev / 10

print
if(sum == x):
    print x,"is Disarium Number"
else:
    print x,"is not Disarium Number"





num = float(input("Enter a number : "))
print

#logic
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")





input = int(raw_input("Enter a number : "))

square = input * input

v = pow(10,len(str(input)))

print
if (square%v)==input:
    print input," is an Automorphic Number"
else:
    print input," is not an Automorphic Number"







# take input from the user
num = int(input("Enter a number: "))

# initialise sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print num,"is an Armstrong number"
else:
   print num,"is not an Armstrong number"





# Definition of the function
def amicable_numbers(x,y):
    sum_x=0
    sum_y=0
    for i in range(1,x):
        if x%i==0:
            sum_x+=i
 
    for k in range(1,y):
        if y%k==0:
            sum_y+=k
            
 
    return sum_x==y and sum_y==x
 
# Program body
n_1=int(raw_input('Enter number 1: '))
n_2=int(raw_input('Enter number 2: '))

print
if amicable_numbers(n_1,n_2):
    print 'The numbers are Amicable! :)'
else:
    print 'The numbers are Not Amicable :('





def sumDigits(num, base=10):
    return sum([int(x, base) for x in list(str(num))])

print sumDigits(1)
print sumDigits(12345)
print sumDigits(123045)
print sumDigits('fe', 16)
print sumDigits("f0e", 16)




def toBaseX(num, base):
    output = []
    while num:
        num, rem = divmod(num, base)
        output.append(rem)
    return output

def sumDigits(num, base=10):
    if base < 2:
        print "Error: Base must be at least 2"
        return
    return sum(toBaseX(num, base))

print sumDigits(1)
print sumDigits(12345)
print sumDigits(123045)
print sumDigits(0xfe, 16)
print sumDigits(0xf0e, 16)





num = float(input('Enter a number : '))
num_sqrt = num ** 0.5

print
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))





alist = list( map(int, raw_input("Enter numbers : ").split()) )

smallest=alist[0]

for small in alist:
    if small < smallest:
        smallest=small

print
print "Smallest number is :",smallest





import random

#Random Function
print(random.choice(['Hello', 'world', 'python']))





def Palindrome_Number(n):
     
    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a * 10
        m = m / 10

    if( n == a):
        print('%d is a palindrome number' %n)
    else:
        print('%d is not a palindrome number' %n)
               
n = input('Enter Number to check for palindromee ')
Palindrome_Number(n)





#using raw_input
age=raw_input('Enter your age : ')
print ("Your age is %d" % int(age));

#using input
number=input('\nEnter any number : ')
print ("You entered %d" % number);





number = int(raw_input("Enter a number : "))

s = 0
square = str(number * number)

for i in range(0,len(square)):
    s += int(square[i:i+1])
    
print
if(s == number):
    print number,"is a Neon Number"
else:
    print number,"is not a Neon Number"





# take input from the user
num = int(input("Display multiplication table of? "))

print

# use for loop to iterate 10 times
for i in range(1,11):
   print num,'x',i,'=',num*i




def isMagic(n):
    s = 0
    d = 0
    number = n
    flag = 0
    while flag == 0:
        while n % 10 == 0:
            n /= 10

        while n% 10 != 0 or n > 0:
            s += (n % 10)
            n /= 10

        if s >= 10:
            n = s
            s = 0
        else:
            flag = 1
            
    if s == 1:
        print number,"is a Magic Number "
    else:
        print number,"is not a Magic Number "

number = int(raw_input("Enter a number : "))

print
isMagic(number)





def lucas(n):
    a = 2
    b = 1
    for i in range(0, n):
         temp = a
         a = b
         b = temp + b
    return a

# take input from the user
nterms = int(input("How many terms? "))

print
# Display the first n lucas numbers.
print "Lucas Series : "
for c in range(0, nterms):
    print (lucas(c)),





# take three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3

print
print "The largest number is :",largest





a=int(raw_input("Enter a number : "))

n=map(int,`a`)

while a>n[0]:n=n[1:]+[sum(n)]

print
if(a==n[0])and(a>9):
    print a,"is a Keith Number"
else:
    print a,"is not a Keith Number"






def k(n):
 n2 = str(n**2)
 for i in range(len(n2)):
  a, b = int(n2[:i] or 0), int(n2[i:])
  if b and a + b == n:
   return n

number = int(raw_input("Enter a upper limit for Kaprekar Numbers : "))
print("Kaprekar Number between the range 1 - "+str(number)+" : ")

print([x for x in range(1,number) if k(x)])






def k(n):
 n2 = str(n**2)
 for i in range(len(n2)):
  a, b = int(n2[:i] or 0), int(n2[i:])
  if b and a + b == n:
   return n

number = int(raw_input("Enter number : "))
if k(number):
        print(str(number)+" is Kaprekar Number")
else:
        print(str(number)+" is not a Kaprekar Number")






def happy(n):
    past = set()   
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        #print(n) # uncomment the code to see the iterated no.
        if n in past:
            return False
        past.add(n)
    return True

number = int(raw_input("Enter the upper limit for happy numbers : "))

print("Happy Numbers between the range 1 - "+str(number)+" : ")
happyn = []
for x in range(1,number):
    if(happy(x)):
        happyn.append(x)
print(happyn)





def happy(n):
    past = set()   
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        #print(n) # uncomment the code to see the iterated no.
        if n in past:
            return False
        past.add(n)
    return True

number = int(raw_input("Enter a Number : "))

if happy(number):
    print(str(number) + " is a Happy Number")
else:
    print(str(number) + " is not a Happy Number")






alist = list( map(int, raw_input("Enter numbers : ").split()) )

largest=alist[0]

for large in alist:
    if large > largest:
        largest=large

print
print "Largest number is :",largest