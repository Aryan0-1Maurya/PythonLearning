import time
 
def sleeper():
    while True:
        # Get user input
        num = raw_input('How long to wait in seconds: ')
 
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
 
        # Run our time.sleep() command,
        # and show the before and after time
        print('Before: %s' % time.ctime())
        time.sleep(num)
        print('After: %s\n' % time.ctime())
 
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()





def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(ndisks=4)




class Authentication(Exception):
 def display(self):
  print "\nAuthentication Failed...";
  
name=raw_input("\nEnter your name: ");
password=int(raw_input("\nEnter your password: "));

try:
 if(password==123):
  print "\nAuthenticated User...";
 else:
  raise Authentication();
except Authentication,a:
 a.display();





from decimal import *

D = Decimal
getcontext().prec = 100
a = n = D(1)
g, z, half = 1 / D(2).sqrt(), D(0.25), D(0.5)
for i in range(18):
    x = [(a + g) * half, (a * g).sqrt()]
    var = x[0] - a
    z -= var * var * n
    n += n
    a, g = x
#to print the calculated pi value
print(a * a / z)




import time
 
def sleeper():
    # Get user input
    num = raw_input('How long to wait: ')

    # Try to convert it to a float
    try:
        num = float(num)
    except ValueError:
        print('Please enter in a number.\n')

    # Run our time.sleep() command,
    # and show the before and after time
    print('Before: %s' % time.ctime())
    time.sleep(num)
    print('After: %s\n' % time.ctime())
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()