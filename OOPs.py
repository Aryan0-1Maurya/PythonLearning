class A(object):
 def __init__(self,a):
  self.a = a;
  
 def display(self):
  print "\nValue of A: ",a;

class B(A):
 def __init__(self,a,b):
  super(B,self).__init__(a);
  self.b = b;
  
 def display(self):
  super(B,self).display();
  print "\nValue of B: ",b;
  
a=100;
b=200;
b1 = B(a,b);
b1.display();





class Employee:
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
print "\nTotal Employee: ",Employee.empCount;





class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print(self.last_name + " eye color is " + self.eye_color)

        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print(self.last_name + " eye color is " + self.eye_color+" and no of toys are "+ str(self.number_of_toys))



avinash = Parent("Shetty","Brown")

rahul = Child("Shetty","Black",5)
avinash.show_info();
rahul.show_info();
print(avinash.eye_color)
print(rahul.eye_color)






class Account(object):
 def __init__(self,name,acc_no):
  self.name = name;
  self.acc_no = acc_no;
  
 def display(self):
  print "\nEmployee Details: ";
  print "\nCustomer name: ",name;
  print "\nAccount number: ",acc_no;
  
class Saving_account(Account):
 def __init__(self,name,acc_no,bal):
  super(Saving_account,self).__init__(name,acc_no);
  self.bal = bal;
	
 def display(self):
  super(Saving_account,self).display();
  print "\nBalance: ",bal;
  
class Account_details(Saving_account):
 def __init__(self,name,acc_no,bal,deposits,withdrawal):
  super(Account_details,self).__init__(name,acc_no,bal);
  self.deposits = deposits;
  self.withdrawal = withdrawal;
  
 def display(self):
  super(Account_details,self).display();
  print "\nDeposits: ",deposits;
  print "\nWithdrawal: ",withdrawal;
  
name=raw_input("\nEnter name: ");
acc_no=int(raw_input("\nEnter account number: "));
bal=int(raw_input("\nEnter balance: "));
deposits=int(raw_input("\nEnter deposit amount: "));
withdrawal=int(raw_input("\nEnter withdrawal amount: "));

ad=Account_details(name,acc_no,bal,deposits,withdrawal);
ad.display();





#method over-loading in python using default argument

class A:
    def first(self, f=None):
        if f is not None:
            print 'Method', f
        else:
            print 'Method without argument'


a = A()
a.first()
print
a.first('with argument')






class Parent(object):  
 def __init__(self):  
  print "\nParent class constructor...";
  
 def display(self):  
  print "\nParent class method...";
  
class Child(Parent):  
 def __init__(self):  
  print "\nChild class constructor...";
  
 def display(self): 
  super(Child,self).display()
  print "\nChild class method...";
  
p = Parent();
c = Child();
c.display();