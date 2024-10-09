#the authors' names are: Serenity and Mac

x = 2
if x < 3:
    print("Small")

x = 5
if x < 3:
    print("Small")

score = 8 #A score on a 10 point quiz
if score > 6:
    print("Nice work!")

#1. if statements make so a specific condition has to be met before executing the next line of code
#2. if statements could be useful IF, for example, you would only want a particular line of code carried out at a certian time, temperature, &c.

for i in range (1, 16):
    if i % 3 == 0:
        print(i, "is divisible by 3")
#this code is going to go through every number from 1 to 15 and if the number is cleanly divisible by three it will print as such

x = input("Number = ")
x = int(x)
if x % 2 == 0:
    print("Even")

x = 2
if x < 3:
    print("Small")
else:
    print("Large")

x = 5
if x < 3:
    print("Small")
else:
    print("Large")

score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:
    print("Nice work!")
else:
    print("Excellent!")

#the else statmetn covers any other result without coding it specifically
#the elif statement adds another condition
#no,every if statement does not need and else statement


for i in range(-2,3):
    if i < 0:
        print(i, " is negative.")
    elif i == 0:
        print(i, " is zero.")
    else:
        print(i, " is positive.")
#this will print negative for -2 through -1, zero for 0, and positive for 1 through 2

x = input("Number = ")
x = int(x)
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

print(3 < 4)
print(4 > 2)
print(type(True))

if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")

#True
#Boolean

print(type(False)) #this will be 'bool'
print(3 == 5) #this will be false

def input_num():
    n = int(input("Please input number here . . ."))
    if n > 10:
        return True
    else:
        return False
        
input_num() #test


