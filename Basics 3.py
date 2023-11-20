def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)
  
add_two_numbers(6,4)

a = 10
print("a=",a,sep= 'dddd', end = '\n\n\n')

a = int(input("Enter first Number: "))
b= int(input("Enter second Number: "))

print(a+b)


L1= ["john", 102, "USA"]
L2 = [1,2,3,4,5,6]

tup = ("Apple", "Mango", "Orange", "Banana")
print(type(tup))
print(tup)

#ordered elements with paired values
employee = {"Name":"John", "Age":29, "salary":250000, "Company":"Google"}
print(type(employee))

# set is a collection of unordered elements

Month= {"January", "February", "March", "April", "May", "June", "July"}
print(Month)

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  


import keyword
print(keyword.kwlist)


print(None == 0)
print(None== "")
print(None== False)
A= None
B = None
print(A== B)


numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]

square = 0

squares = []

for value in numbers:
  square = value ** 2
  squares.append(square)
print("the list of square is",squares)



# creating the list of numbers  
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
  
# initializing a variable that will store the sum  
sum_ = 0  
  
# using for loop to iterate over the list  
for num in numbers:  
     
    sum_ = sum_ + num ** 2   
  
print("The sum of squares is: ", sum_)  


my_list = [3,5,6, 8, 4]
for iter_var in range(len(my_list)):
  my_list.append(my_list[iter_var] + 2)
print(my_list)

# Creating a dictionary of records of the students  

student_name_1 = 'Itika'
student_name_2 = 'Parker'


#dictionary for records of students
records= {}


