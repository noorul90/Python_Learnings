list = ["Noorul", 28, 5.11, "male"]
string = "Noorul"

for value in list:
    print(value, type(value))
print("-------------------")
for value in string:
    print(value, type(value))
print("-----------------------")
for value in [1,2,"noorul"]:
    print(value, type(value))
print("-------------------")
for value in range(4):
    print(value, type(value))
print("---------------")
for value in range(10,21,2):   #start from 10 end at 20 incremented by 2
    print(value, type(value))
print("-----------------")
for value in range(20,10,-3):           #print in reverse order
    print(value, type(value))