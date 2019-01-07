#by default recursion limit is 1000, bur we can customize it
import sys
print("default recursion limit is: ", sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("customized recursion limit is : ", sys.getrecursionlimit())

i=0
def doSomething():
    global i
    i += 1
    print("Hi Noorul ", i)
    doSomething()

doSomething()