
import pandas as pd
import numpy as np

num = []

num.append(21)
num.append(40.5)
num.append("String")

print(num)


#Multiplication

num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)



num1 = 34
if (num1>12):
   print("Numerable")
elif(num1>35):
    print("Nope")
else:
    print("great")
    
    
if 's' in 'geeksforgeeks':
     print('s is part')
else: 
     print('s is not part of')
     
     
for i in 'geeksforgeeks':
    print(i, end= " ")
    
    
print("\r")

print({} is {})


for i in range(10):
  print(i, end=" ")
  
  
  if i == 6:
     break
   
   
i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
       print(i, end= " ")
    i += 1
      
      
i = 20
if (i==10):
    print("i is 10")
elif (i==20):
    print("i is 20")
else:
    print("i is not here")
    
    
    
def fun():
    print("Inside Function")
    
fun()


def fun():
    s = 0
    
    for i in range(11):
        s += i
    return s
  
print(fun())


#----------

def fun():
    s = 0
    
    for i in range(10):
        s += i
        yield s
        
        
for i in fun():
    print(i)
    
    
class Dog:
   attr1 = "mammal"
   attr2= "dog"

   def fun(self):
       print("You are a ", self.attr1)
       print("You are a ", self.attr2)
       
       
rodger = Dog()

rodger.fun()


import math as gfg

print(gfg.factorial(5))


n = 10
for i in range(n):
    pass
  


n = 10
for i in range(n):
    pass


g = lambda x: x*x*x

print(g(6))


from math import factorial
import math
print(math.factorial(10))


a = 4
b = 0

try:
  
  k = a//b
  print(k)
  
  
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
    
  
print("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print(a / b)


temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")
  
  

def add():
    c = a + b
    print(c)
    
add()
  

def fun():
    var1 = 10
    
    def gun():
        nonlocal var1
        
        var1 = var1 + 10
        print(var1)
        
    gun()
    
fun()


count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()



s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
  

n = (1 * 2 * 3 + 7 + 8 + 9)

x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}
 
j = 1

while(j <= 5):
  print(j)
  j = j +1
  
  
  a = 10
  b = 4
  

  print(~a)
     
     
def divide(x, y):
  try:
    result = x // y
    print("yeah!",result)
  except ZeroDivisionError:
    print('sorry!')
    
divide(3,2)



num = int(input("Enter number here:"))
print(num)


num = int(input("Enter number here:"))
print("the int is:",num)

num = int(input("Enter an integer: "))
print(num)

num = int(int(input("enter a num:"))
print(num, " ", type(num))



           
print("type of number", type(num))


floatNum = float(input("Ent the num here: "))
print(floatNum, " ", type(floatNum))



num1 = int(input())
num2 = int(input())

print(num1 +num2)
  
  

a = 10
b = 20
c = a
 
print(a is not b)
print(a is c)


a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a < b else b
 
print(min)


# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)


# Precedence of 'or' & 'and'
name = "Alex"
age = 0
 
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
    
    
class Myclass:
  def __init__(self, value):
      self.value = value
      
  def __truediv__(self, other):
      return Myclass(self.value & other.value)
  
a = MyClass(True)
b = MyClass(False)
  
c = a / b


letter = "A"

if letter == "B":
  print("letter is B")
  
else:
  
  if letter == "C":
    print("letter is c")
    
  else:
    
    if letter == "A":
      print("letter is A")
        
    else:
      print("letter is not A, B,C")
      
      
class A:
  def __init__(self, a):
      self.a = a
      
  def __add__(self, o):
      return self.a + o.a
    
  ob1 = A(1)
  ob2 = A(2)
  ob3 = A("Geeks")
  ob4 = 
      

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "

for i in text:
    a = a+str(i[0]).upper()
    
print(a)



