#set can't contains duplicates elemnts or set is a unorderd collection of unique element
#set is similor to list except it can't contain duplicate value 
numsSet = {1,2,5,8,4,'raaj'}
print(numsSet)
#passing duplicate element will not return any error but duplicate is overriden
nums = {1,2,5,9,5,9,15}
print(nums)
nums.add(55)
print(nums)
nums.remove(5)
print(nums)
nums.pop()
print(nums)
nums.clear()
print(nums)