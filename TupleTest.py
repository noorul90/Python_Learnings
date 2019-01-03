#list is mutable but tuple is not mutable means once you create the tuple you can't change value in tuples

numsTuple = (12,15,14,52,44)  #12,15,14,52,44
nums = 14,52,55,25
print(type(nums), nums)
print(numsTuple)
print(numsTuple[1])
#immutable nature
#numsTuple[1]=15 #gives error beacause we can't change the value
#print(numsTuple)