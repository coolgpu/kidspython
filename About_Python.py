Python for its scope doesn’t depend on the braces ( { } ), instead it uses indentation for its scope.

In other programming languages like C, C++ and Java, you will need to declare the type of variables but in Python you don’t need to do that. Just type in the variable and when values will be given to it, then it will automatically know whether the value given would be a int, float or char or even a String.


# Python program to declare variables 
myNumber = 3
print(myNumber) 
  
myNumber2 = 4.5
print(myNumber2) 
  
myNumber ="helloworld"
print(myNumber) 

Python have 4 types of built in Data Structures namely List, Dictionary, Tuple and Set. 

# Python program to illustrate list  
  
# creates a empty list 
nums = []  
  
# appending data in list 
nums.append(21) 
nums.append(40.5) 
nums.append("String") 
  
print(nums) 

# Comments:
# is used for single line comment in Python
""" this is a comment """ is used for multi line comments


# Python program to illustrate 
# getting input from user 
name = input("Enter your name: ") 
  
# user entered the name 'harssh' 
print("hello", name) 
# accepting integer from the user 
num1 = int(input("Enter num1: "))  
num2 = int(input("Enter num2: ")) 
  
num3 = num1 * num2 
print("Product is: ", num3) 



# Python program to illustrate 
# selection statement 
  
num1 = 34
if(num1>12): 
    print("Num1 is good") 
elif(num1>35): 
    print("Num2 is not gooooo....") 
else: 
    print("Num2 is great") 

	

#Functions

#You can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. Python used the keyword ‘def’ to define a function.
#Syntax:

#def function-name(arguments):
            #function body
# Python program to illustrate 
# functions 
def hello(): 
    print("hello") 
    print("hello again") 
  
# calling function 
hello()         



# Python program to illustrate  
# function with main 
def getInteger(): 
    result = int(input("Enter integer: ")) 
    return result 
  
def Main(): 
    print("Started") 
# calling the getInteger function and  
# storing its returned value in the output variable 
    output = getInteger()      
    print(output) 
  
# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 

	
	
#Iteration (Looping)
for step in range(5):     
    print(step) 
	
#Modules

# Python program to illustrate 
# math module 
import math 
  
def Main(): 
    num = float(input("Enter a number: ")) 
    # fabs is used to get the absolute value of a decimal 
    num = math.fabs(num)  
    print(num) 
if __name__=="__main__": 
    Main() 

	
	
#Namespaces and Scope in Python
# Scope : A scope defines the hierarchical order in which the namespaces have to be searched in order to obtain the mappings of name-to-object(variables). It is a context in which variables exist and from which they are referenced. It defines the accessibility and the lifetime of a variable. Let us take a simple example as shown below:

#Local Scope :
#Local scope refers to variables defined in current function.Always, a function will first look up for a variable name in its local scope. Only if it does not find it there, the outer scopes are checked.
pi = 'global pi variable'
def inner(): 
    pi = 'inner pi variable'
    print(pi) 
  
inner() 

# Local and Global Scopes :
# If a variable is not defined in local scope, then, it is checked for in the higher scope, in this case, the global scope.

# Global Scope 
  
a = 'global variable a'
b = 'global variable b'
def inner(): 
    a = 'inner variable a'
    print(a)
	print(b)
  
inner() 
print(a) 
print(b) 

# Local, Enclosed and Global Scopes :
# For the enclosed scope, we need to define an outer function enclosing the inner function, comment out the local pi variable of inner function and refer to pi using the nonlocal keyword.
# Enclosed Scope 

pi = 'global pi variable'

def outer(): 
	pi = 'outer pi variable'
	def inner(): 
		# pi = 'inner pi variable' 
		nonlocal pi 
		print(pi) 
	inner() 

outer() 
print(pi) 




# var1 is in the global namespace  
var1 = 5
def some_func(): 
  
    # var2 is in the local namespace  
    var2 = 6
    def some_inner_func(): 
  
        # var3 is in the nested local  
        # namespace 
        var3 = 7

		
		
# Python program processing 
# global variable 

count = 5
def some_method(): 
	global count 
	count = count + 1
	print(count) 
some_method() 




# Python program showing 
# a scope of object 
  
def some_func(): 
    print("Inside some_func") 
    def some_inner_func(): 
        var = 10
        print("Inside inner function, value of var:",var) 
    some_inner_func() 
    print("Try printing var from outer function: ",var) 
some_func() 


a = 1

# Uses global because there is no local 'a' 
def f(): 
	print 'Inside f() : ', a 

# Variable 'a' is redefined as a local 
def g():	 
	a = 2
	print 'Inside g() : ',a 

# Uses global keyword to modify global 'a' 
def h():	 
	global a 
	a = 3
	print 'Inside h() : ',a 

# Global scope 
print 'global : ',a 
f() 
print 'global : ',a 
g() 
print 'global : ',a 
h() 
print 'global : ',a 




#Multi-Line Statements: 
# Any statement containing opening parentheses (‘(‘), brackets (‘[‘), or curly braces (‘{‘) is presumed to be incomplete until all matching parentheses, square brackets, and curly braces have been encountered.
# Explicit Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

# Implicit Line Continuation 	
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']

person_1 = 18
person_2 = 20
person_3 = 12
  
if ( 
   person_1 >= 18 and
   person_2 >= 18 and
   person_3 < 18
   ): 
    print('2 Persons should have ID Cards') 

x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}	
	 
# Indentation
# A block is a combination of all these statements. Block can be regarded as the grouping of statements for a specific purpose. Most of the programming languages like C, C++, Java use braces { } to define a block of code. One of the distinctive features of Python is its use of indentation to highlight the blocks of code. Whitespace is used for indentation in Python. All statements with the same distance to the right belong to the same block of code. If a block has to be more deeply nested, it is simply indented further to the right. 



Swap two variables
x = 10
y = 99
x,y = y,x


Nonmutable
x = 20
print(id(x))
x = x + 1
print(id(x))

y = [1, 2, 3]
print(id(y))
y.append("good")
print(id(y))
