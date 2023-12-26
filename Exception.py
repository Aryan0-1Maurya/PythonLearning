#program that uses try-except, else

while True:
    # Read int from console.
    denominator = int(raw_input("Enter number : "))

    # Use int as denominator.
    try:
        i = 1 / denominator
    except:
        print("Error")
        raise
    else:
        print("OK")



class AgeNegative(Exception):  
 def display(self):
  print "\nAge is negative...";
  
age = int(raw_input("\nEnter your age: "));
try:
 if(age<0):
  raise AgeNegative();
 else:
  print "\nNo Exception Raised...";
except AgeNegative,e:
 e.display();