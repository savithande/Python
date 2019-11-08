# dictionary is the set of key,value pair
# syntax of the creating dictionary is --> dict_name = { 'key' : 'value'}

dict = {'name' : 'Python', 'language' : 'scripting'}

# to print the dictionary, the syntax is --->print(dict)

print (dict)

# to print the values of the dictionary by using its keys

# syntax --> dict_name['key_name']

print(dict['name'])
print ("------------------------------------------------------------------")

# to print the key and value separately
American_first_lady = {'name':'michelle obama','DOB':'17/01/1964','place':'chicago'}
for key,value in American_first_lady.items():
    print ("key is %s" % key)
    print ("the value is %s " % value)
    print ("----------------------------------")

print ("---------------------inserting to the key values into the dictionary----------------------------------")

# insert the elements into the dictionary
# Syntax ----> dict_name["kay_value"] = "value"

songs = {}
songs["name"] = "thum se hi"
songs["language"] = "hindi"

print(songs)
print("------------------------------------------------=")

# combining two dictionaries
# syntax dict_name1.update[dict_name2]
American_first_lady1 = {'name':'michelle obama','DOB':'17/01/1964','place':'chicago'}
American_first_lady.update(songs)
print(American_first_lady)
print("\n")
print("----------------------deleting the key-value from the dictionary -----------------------")
# by using the del method
del American_first_lady["name"]
print(American_first_lady)
print("----------------------------------")
# by using the pop method
American_first_lady.pop("language")
print(American_first_lady)


