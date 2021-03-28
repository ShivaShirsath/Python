
def main():
    name = input("Enter your name : ")
    print( "Hello", name, "!" )
    
if __name__ == "__main__" :
    main()


#Below is a simple Python program that creates a class with single method.

# A simple example class 
class Test:
       
    # A sample method  
    def fun(self):
        print("Hello Class, i am function") 
  
# Driver code
obj = Test()
obj.fun()

# The self

'''
Class methods must have an extra first parameter in method definition. We do not give a value for this parameter when we call the method, Python provides it
If we have a method which takes no arguments, then we still have to have one argument – the self. See fun() in above simple example.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
'''

# The __init__ method

'''
The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
'''

# A Sample class with init method 
class Person: 
  
    # init method or constructor  
    def __init__(self, name): 
        self.name = name 
  
    # Sample Method  
    def say_hi(self): 
        print('Hello, my name is', self.name) 
  
p = Person('Shiva')
p.say_hi()

# Class and Instance Variables (Or attributes)

'''
In Python, instance variables are variables whose value is assigned inside a constructor or method with self.
'''

# Class variables are variables whose value is assigned in class.

'''
Python program to show that the variables with a value assigned in class declaration, are class variables and variables inside methods and constructors are instance variables. 
'''

# Class for Student 
class Student: 
  
    # Class Variable 
    stream = 'Computer'             
  
    # The init method or constructor 
    def __init__(self, roll): 
    
        # Instance Variable     
        self.roll = roll        
   
# Objects of Student class 
a = Student(101) 
b = Student(102) 
   
print("a.stream", a.stream)  # prints "cse" 
print("b.stream", b.stream)  # prints "cse" 
print("a.roll", a.roll)    # prints 101 
   
# Class variables can be accessed using class name also 
print("Student.stream", Student.stream, end="\n\n") # prints "cse" We can define instance variables inside normal methods also.

# Python program to show that we can create instance variables inside methods 
   
# Class for Student 
class Student: 
      
    # Class Variable 
    stream = 'Computer Technology'      
      
    # The init method or constructor 
    def __init__(self, roll): 
          
        # Instance Variable 
        self.roll = roll             
  
    # Adds an instance variable  
    def setAddress(self, address): 
        self.address = address 
      
    # Retrieves instance variable     
    def getAddress(self):     
        return self.address    
  
# Driver Code 
a = Student(101) 
a.setAddress("Kolhar, Maharashtra") 
print("Address is", a.getAddress())

# Data hiding

'''
In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside.
'''

class Class: 
  
    # Hidden member of MyClass 
    __hiddenVariable = 0
    
    # A member method that changes  __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 
   
# Driver code 
Object = Class()      
Object.add(25) 
Object.add(55)
print()
  
# This line causes error 
print (Object.__hiddenVariable)

# We can access the value of hidden attribute by a tricky syntax:

'''
A Python program to demonstrate that hidden  members can be accessed outside a class
'''

class Class: 
  
    # Hidden member of MyClass 
    __hiddenVariable = 10
  
# Driver code 
Object = Class()      
print(Object._Class__hiddenVariable)

# Printing Objects

'''
Printing objects gives us information about objects we are working with. In C++, we can do this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class. In Java, we use toString() method. In python this can be achieved by using __repr__ or __str__ methods.
'''
class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "\n\tFrom repr method of Test \n\ta:%s \n\tb:%s\n" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: \n\ta is %s \n\tb is %s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__()

# Important Points about Printing:

'''
If no __str__ method is defined, print t (or print str(t)) uses __repr__.
'''

class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "From repr Test a:%s b:%s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t)  

'''
If no __repr__ method is defined then the default is used.
'''

class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
# Driver Code         
t = Test(1234, 5678) 
print(t)

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Class

class Class:
    pass                                     

print("Class :", Class())               

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Object

Object = Class()                        

print("Object :", Object)            

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Class Constructor

class Constructor:           
    
        def __init__(self, name): 
            self.name = name       

Object = Constructor("Constuctor")  
print("Self name :", Object.name)              

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Attributes
class Attributes:
    
    attribute = "Class Attribute"              
    
    def __init__(self, instance):
        self.instance = instance
        
atrCheck = Attributes("Instance Attribute")

print("Class Attribute:", atrCheck.attribute)
print("Instance Attribute :", atrCheck.instance)

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Class Method (Function)

class Method:   

    def __init__(self, instance):
        self.instance = instance 

    def method(self):                 
        return "This is Method and Attribute : %s" % self.instance
        
Object = Method("Instance Attribute")
print(Object.method())

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Creating more than one object of a class

class MoreObject:   

    def __init__(self, instance):
        self.attribute = instance 

    def method(self):                 
        return self.attribute

obj1 = MoreObject("Object 1")        
obj2 = MoreObject("Object 2")
print("This is Method and Attributes :\n\t", obj1.method(), "\n\t", obj2.method())

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Inheritance in Python

class Parent:
    behaviour = "Simple"

class Child(Parent):
    pass 

print(Parent, "Behaviour :", Parent.behaviour)
print(Child, " Behaviour :", Child.behaviour)

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

#Encapsulation

class Encapsulation:
    variable = "public variable"                  
    _variable = "protected variable"            
    __variable = "private variable"              

encaps = Encapsulation()
print("Security :    :", encaps.variable)
print("Security : _  :", encaps._variable)
print("Security : __ :", encaps._Encapsulation__variable)

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Polymorphism : multi-form

class Form1:
  def morphism(self):
    print("Form 1")

class Form2:
  def morphism(self):
    print("Form 2")
    
class Form3:
  def morphism(self):
    print("Form 3")

for poly in (Form1(), Form2(), Form3()):
    poly.morphism()
  
print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")

# Data Abstraction : hiding background details

from abc import ABC, abstractmethod

class Abstract(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def abstractMethod(self, done):
        pass
        
class new(Abstract):
    def abstractMethod(self, done):
        print(f"The {self.name} is now {done}")
        
Object = new("Abstract Method")

Object.abstractMethod("Competed")

print("\no()shiva[{:::::::::::::::::::::::::::::::::::::::>\n")
