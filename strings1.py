# single quote character

str = 'Python'
print(str)
# fine  the type of variable
print(type(str))
print("\n")

# double quote character

str = "Python"
print(str)
# fine  the type of variable
print(type(str))
print("\n")

# triple quote example

str = """Python"""
print(str)
# fine  the type of variable
print(type(str))
print("\n")

# methods of string
# 1) finding the index value
string = "Python"
print("Python".index("t"))
print("Python_programing_language".index("_"))
print ("\n")

# join the list of strings by using join condition

combine_string = "%".join(["1","2","3"])
print(combine_string)
print("\n")

#  split the string based on the condition by using the split()
print("1:2:3:4".split(":"))
print("1 2 3 4".split(" "))
print("1,2,3,4,5,6".split(","))
print("\n")

# accessing the individual character in the string
# by using the index values of the given string
# the python index value stating with "0"

string = "Python"
print(string[4])
print(string[0])
print("\n")

# formatting methods usage examples
print("hii, my name is %s" % ("Python"))
print("%s is a one of the %s language" % ("Python","scripting"))
print("\n")

# truth value testing of string using boolean(bool) keyword
print(bool("")) # '0' argument method
print(bool("Python")) # with argument method


