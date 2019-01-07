#example of function and different types of arguments in python

def greet():
    print("Hello Noorul")
    print("how are you!!!")

greet()

def add(a, b):
    x = a + b
    print("sum of a and b : ", x)

add(4,3)

def retResutFromFunc(x, y):
    return x+y

sum = retResutFromFunc(50,49)
print("sum: ", sum)

#function that return two values
def add_subs(a,b):
    x=a+b
    y=a-b
    return x,y

result1, result2 = add_subs(41,25)
print(result1, result2)

#function arguments in python
def updateX(x):
    print("address of x : ", id(x))
    x=10
    print("id of x: ", id(x))
    print("x: ", x)
#pass by vlue or call by value--> here we are passing the value not the address of value
updateX(12) #OR

#pass by reference or call by reference---> here we are passing address not the value
a=15
print("address of a: ", id(a))
updateX(a)
print("a : ", a)
#conclusion is in python there is no concept like call by value and call by reference

#Understanding different types of arguments in function i.e formal and actual arguments
#actual arguments has 4 types i.e position, keyword, default and variable length
def human(name,age):  #here name and 28 are formal arguments
    print(name)
    print(age+10)

human("noorul",28)  #here noorul, 28 is actual arguments, also position argument
human(age=28, name="noorul") #keyword arguments

def defaultargs(name, age=18):  #here age is default arguments, if we didn't pass age value when we called function then bydefaukt it take 18
    print("name: ", name)
    print("age: ", age)

defaultargs("Noorul")
defaultargs("noorulislam", 28)

#variable length arguments
def sum(a, *b):  #b is variable length arguments that except as tuples
    print(a)
    print(b, type(b))
    c = a
    #d = a+ b #not working because b is tuples
    for i in b:
        c = c+i
    print("var args sum is: ", c)

sum(10,20,30,40,25)
sum(2,3,4,5)

#keyworded variable length arguments declared by **
def employee(name, **data):
    print("name ", name)
    print("kwargs employee data: ", data, type(data))

    for i,j in data.items():
        print("key: ", i, "value: ", j)


employee("noorul", age=28, empid=123456, city="delhi")

