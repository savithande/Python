# in python there are 2 types of the condition methods are there
# one is looping and another one is condition

# looping statements
# for loop statement
print ("*******************************************for loop********************************************")
for i in range (10):
    print (i)
    print("\n")

# for loop using in list

colours = ["red","black","white","gry","yellow","green","blue"]
print(colours)
print("\n")

for colour in colours:
    colour_size = 0
    for no_of_color in colour:
        colour_size += 1
        print("no of colours : %s and it has the length : %s" %(colour,colour_size))
print ("\n")

# looping with both indexes and values
for index, colour in enumerate(colours): # enumerate used to returns the index value and its item
    print("index value is : %s",index)
    print("color is : %s",colour)
    print ("-----------------------")
print ("\n")
print ("*******************************************nested for loop********************************************")

# nested for loop
for i in range(1,11):
    for j in range(1,11):
        print ('%d * %d = %d' %(i,j,i*j))
    print ("-------------------------")
print ("\n")
print ("*******************************************while loop********************************************")
# while loop
colours = ["red","black","white","gry","yellow","green","blue"]
length = len(colours)
i = 0   # initialization
while(i<length): # condition
    print(colours[i])
    i = i + 1 # increment
print ("\n")
print ("*******************************************if-else condition********************************************")

# condition statements
num = 45
if (num != 45):
    print("the num is not correct")
else:
    print ("the num is correct")
print("\n")

print ("*******************************************if-elif condition********************************************")

num1 = 10
num2 = 30
num3 = 40

if ((num1 > num2) and (num1 > num3)):     # condition
    print ("num1 is greater: ",num1)
elif((num2 > num1) and (num2 > num3)):
    print("num2 is greater: ",num2)
else:
    print ("num3 is greater: ",num3)
print ("\n")
print ("*******************************************nested if-else condition********************************************")


if(num2 > 20):  # condition
    if(num2 < 40):
        print("the num2 lise between 20 and 40")
    else:
        print("the num2 not lise between 20 and 40")

