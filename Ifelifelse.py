x = 16
r = x % 2

if r==0:
    print("x is even")
    if x>5:
        print("x is greater than 5")
    else:
        print("not greater than 5")
elif r==1:
    print("x is odd")
else:
    print("wrong input")

print("Bbye.....")