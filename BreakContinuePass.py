#break, vending machine logic
avPhone = 5
x  = int(input("Enter the phone "))
i=1
while i <= x:
    if i>avPhone:
        print("out of stock")
        break                  #jump out of the loop or break the further iteration
    print("phone")
    i+=1

print("bbyee")

#continue, print the number between 1-20 which is not divisible by 3 or 5
for i in range(1,21):
    if i%3==0 or i%5==0:
        continue         #skip the perticular iteration and start from next iteration
    print(i)

print("BBByeee")

#pass, don't print value of the number between 1-20 which is odd
for i in range(1,21):
    if (i%2 != 0):
        pass             #for odd number don't do anything
    else:
        print("event number : " , i)

print("Bbbyyyyeee")