i = 1
while i<=5:
    print("Nooruli ", i)
    i = i+1
print("===========================")
j = 5
#nested while loop
while j>=1:
    print(" Noorulj", j, end="") #don't print the value on new line
    j = j-1
    k = 1
    while k<=3:
        print(" awesome ", end="") #don't print the value from new line
        k = k + 1
    print()
print("loop execution completed ")