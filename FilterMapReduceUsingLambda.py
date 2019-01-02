#use of filter(), map() and reduce() function
from functools import *

numsList = [1,2,5,8,3,54,86,24]

def even_func(n):
    return n%2==0

def double_val(n):
    return n*2

def add_all(a,b):
    return a+b;

#using normal function
#evenNums = list(filter(even_func, numsList))

#using lambda expression
evenNums = list(filter(lambda n : n%2==0, numsList))

print(evenNums)

#use of map
#using normal function
#doubleVal = list(map(double_val, numsList))

#using lambda
doubleVal = list(map(lambda n : n*2, numsList))
print(doubleVal)

#use of reduce()
#add all the value in list to reduce the list
#addAll = reduce(add_all, numsList)

#using lambda expression
addAll = reduce(lambda a,b: a+b, numsList)
print(addAll)
