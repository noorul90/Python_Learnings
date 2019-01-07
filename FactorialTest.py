#find factorial of a number using for loop

def fact(n):
    f=1
    for i in range(1, n+1):
        f = f*i

    return f

num = int(input("Enter the number: "))
fac = fact(num)
print("factorial of {} is {} ".format(num, fac))

#using recursion
def recur(n):
    if n==0:
        return 1
    if n==1:
        return 1

    return n*recur(n-1)

recResult = recur(6)
print("recResult: ", recResult)

