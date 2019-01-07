#func that takes list and return even and odd numbers count
def even_odd(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even += 1
        else:
            odd += 1

    return even,odd

list = [10,20,5,3,36,1,8,55,41,15,22,88,15,19]
even, odd = even_odd(list)
print("Even count: {} and Odd count: {}".format(even, odd))

#take the number of name from user and count no of names who has more that 5 characters

def countCgaracter(nameList):
    nameCount=0
    for name in nameList:
        if len(name)>5:
            nameCount += 1
        else:
            print("name \"{}\" contains less than 5 characters".format(name) )

    return nameCount

names = ["Raaj", "Noorul", "Rajesh", "Aniket", "Willium", "Robert", "Henry", "Edword"]
namesCount = countCgaracter(names)
print("name count: ", namesCount)