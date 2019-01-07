a = 10

def something():
    global a     # if u want to access global variable inside function
    a = 12
    print("local a : ", a)  #prefrence is always first in local the in global

something()
print("outside func a: ", a)

#if we want to access both global and local variable in function that has same name
x=10
print(id(x))
def doSomething():
    x=15
    y = globals()["x"]
    print("y is ", y)
    print(id(y))  #here id of x and y are same that means pointing to same variables
    globals()["x"] = 50 #changing global var value inside local scope
    print("x is ", x)

doSomething()
print("x from outside ", x)