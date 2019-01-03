'''
A dictionary in Python is a collection of unordered values accessed by key rather than by index
Dictionary in Python is an unordered collection of data values, used to store data values like a map,
which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair
key must be unique but value may be duplicated
'''

numsDict = {"name":"raaj", "age":25, "gender":"male"}
print(numsDict)
print(numsDict["name"])
print(numsDict.keys(), type(numsDict.keys()))
print(numsDict.values(), type(numsDict.values()))
print(numsDict.items())
print(numsDict.get('name'))
#aading entry/item to existing dictionary
numsDict["id"] = 46617
numsDict["city"] = ["A","B","C"]
numsDict[1] = 1,2,3
print(numsDict)
#replacing item value using key
numsDict["city"] = "gurgaon", "delhi", "bangalore"
print(numsDict)

# Initial Dictionary
dict = {
    5: 'Welcome', 6: 'To', 7: 'Geeks','A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},'B': {1: 'Geeks', 2: 'Life'}
}
print("Initial Dictionary: ")
print(dict)

# Deleting a Key value
del dict[6]
print("\nDeleting a specific key: ")
print(dict)

# Deleting a Key from Nested Dictionary
del dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(dict)

# Deleting a Key using pop()
dict.pop(5)
print("\nPopping specific element: ")
print(dict)

# Deleting a Key using popitem()
dict.popitem()
print("\nPops first element: ")
print(dict)

# Deleting entire Dictionary
dict.clear()
print("\nDeleting Entire Dictionary: ")
print(dict)

#======================================================
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

#==========================================================

# Python program to demonstrate accesing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# accessing a element using key
print("Acessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Acessing a element using key:")
print(Dict[1])

# accessing a element using get() method
print("Acessing a element using get:")
print(Dict.get(3))