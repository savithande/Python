# creations of functions in python :- functions is a name of the block of code

# creation of function\

def add_two_numbers(num1,num2): # def(used to tell fun is defined) name_of_block(arguments):
    result = num1 + num2        # statements
    return result               # return value
# call the function with arguments and the result will be assign to the new variable
sum = add_two_numbers(10,20)
print (sum)  #to print the assigned value
print ("\n")

# without arguments how to call the function
def days():
    print("mon,tue,wed,thu,fri,sat,san")
days()


