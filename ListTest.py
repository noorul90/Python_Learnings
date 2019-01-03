# List is ordered collection of duplicate or unique element unlike set.
# list can contain heterogeneous type of element

numList = [2,32,56,85,52]
print(numList[0])
print(numList[4])
print(numList[2:]) #print element start from 2nd index
print(numList[-1])
print(numList[-2:]) #print elemnet index start from -2 index
print(numList[2:4]) #print elemnt between 2 to 4-1 index
namesList = ["noorul","raaj","shoeb"]
print(namesList)
miscl = [10.2, 12, "alita"]
print(miscl)
nestedList = [namesList,miscl]
print(nestedList)
#append -> it will add the element at last index
numList.append(99)
print(numList)
#clear
#numList.clear()
#print("clear : " , numList)
#insert -> it will insert the elemnet in between existing elemnt based on index
numList.insert(4, 204) #at 4th index inserted elemnt 204
print("insert : " , numList)
numList.remove(56) #remove elemnt 56 from list
print(numList)
numList.pop(2) #remove number at index 2 i.e 85 here and return removed element
print(numList)
numList.pop() #remove last element from listy i.e 99 here and return removed element
print(numList)
del numList[2:] #remove the elemnt start from 2nd index
print(numList)
numList.extend([25,42,44,12]) #adding multiple value in list at a time
print(numList)
print(min(numList)) # find minimun value in list
print(max(numList)) #similarly to find maximum value in a list
print(sum(numList)) #to find sum of all the value
numList.sort() # get all list value in sorted format
print(numList)
