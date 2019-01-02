from array import *

n = int(input("Enter length of array"))

arr = array('i', [])

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print("final array is : ", arr)

#search a perticular element in array and print ots index number

searchElement = int(input("Enter the elemnt for search "))
k=0
count = 0
for e in arr:
    if e==searchElement:
        count += 1
        print("index of ", e ," is ", k)
        break

    k+=1

if count==0:
    print("element not found in array...")

#using inbuilt function find the index of element
#print(arr.index(searchElement))