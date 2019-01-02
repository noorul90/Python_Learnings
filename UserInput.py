#by default input() function gives you string format value
'''
x = input("Enter 1st number ")
print(type(x))
a = int(x)
y = input("Enter 2nd number ")
print(type(y))
b = int(y)
z = a + b
print(z)
'''
'''
x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number "))
z = x + y
print(z)
'''

char = input("Enter a character ")[0]
print(char)

result = eval(input("Enter the expression for result "))
print(result)

#command line input
import sys
x = int(sys.argv[1]) #2
y = int(sys.argv[2]) #5
z = x + y
print(z)
#run above code from cmd like python UserInput.py 2 5
