#array will contain all the value of same type unlike list, in python aarays are not fix in side unlike java, u can expand and shrink it
from array import *

vals = array('i', [1,2,5,6])
print(vals)

#creating new array from existing one
newArray = array(vals.typecode, (a*a for a in vals))
print("new array ", newArray)

#print(vals.buffer_info()) #output format is (address, array_size)
#print(vals.typecode)
#vals.reverse()
#print(vals)
print(vals[0])
for i in range(len(vals)):
    print(vals[i])

#OR
for e in vals:
    print(e)

#declaring char arrays
chararr = array('u', ['a','b', 'c', 'd'])
print(chararr)
for ch in chararr:
    print(ch)