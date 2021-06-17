# Given list x = [100,110,120,130,140,150], 
# use list comprehension to create another list containing each number in the list multiplied by 5.  
x = [100,110,120,130,140,150]
y=[]
for a in x :
    z= a*5
    y.append(z)
print(y)

# Write a function named divisible_by_three that accepts a number n 
# and prints all numbers from 1 to n that are divisible by 3. 

def divisible_by_three(n):
    x= range(1,n)
    for a in x :
        if(a%3==0):
            print(a)
divisible_by_three(10)

# Given the nested list x = [[1,2],[3,4],[5,6]], 
# write a function that flattens the list and returns it as [1,2,3,4,5,6]

def flatten_number():
    x=[[1,2],[3,4],[5,6]]
    y=[]
    for a in x:
        len(x)

# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. 
# Example:smallest([3,6,8,2,4,1,5,7]) returns 1

# def smallest(x):
#    for a in x:
#        x.count(a)
#        print( a<a+1)
           
# smallest([3,6,7,8,2,4,1,5,7])
# Write a function that accepts list x below 
# and uses a set to remove the duplicate letters and returns the list without duplicates
# x = ['a','b','a','e','d','b','c','e','f','g','h']

def duplicate(x):
    y=[]
    for element in x:
        if x.count(element)>1:
            x.remove(element)
            y.append(element)
    print(y)
duplicate(['a','b','a','e','d','b','c','e','f','g','h'])
# Write a function named divisible_by_seven that; using the range function 
# and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.

def divisible_by_seven():
    y=[]
    x= range(100,200)
    for a in x:
        if a%7==0:
            y.append(a)
    return y
print(divisible_by_seven())

# Given this list of students containing age and name,  
# students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], 
# write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.
from datetime import datetime
from typing import ValuesView
def greeting():
    students = [
        {"age": 19, "name": "Eunice"}, 
        {"age": 21, "name": "Agnes"}, 
        {"age": 18, "name": "Teresa"}, 
        {"age": 22, "name": "Asha"}
        ]
    now= datetime.now()
    
    
    print( f"Hello {students}you were born in the year ")
greeting()

#8.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        A=self.width*self.length
        return A
    def perimeter(self):
        addition=self.length+self.width
        P=2*addition
        return P