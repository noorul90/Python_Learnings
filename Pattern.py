#patter for square
for i in range(4):
    for j in range(4):
        print("* ", end="")
    print()
print("----------------------------")
#patter for right angle trangle
for i in range(4):
    for j in range(i+1):
        print("* ", end="")
    print()
print("-----------------------------")
#pattern for vertical right angle triangle
for i in range(4):
    for j in range(4-i):
        print("* ", end="")
    print()