# list is a data structure it is used to store the multiple data
# creating a list

Tech_languages = ["Python","java","Ruby","C"]
print (Tech_languages)
print ("************************************************************************************")

# to print the 1st language by using the index value
print (Tech_languages[0])
print ("************************************************************************************")


# to print the  2nd language
print (Tech_languages[1] )
print ("************************************************************************************")


Tech_languages = [["Python","Java","Ruby"],["html","css","bootstrap"]]
print (Tech_languages)
print ("************************************************************************************")


# to print individual argument
print (Tech_languages[0]) # access the 1st index of the list
print ("************************************************************************************")

print (Tech_languages[0][1]) # access the 1st index and 1st element of the list
print ("************************************************************************************")

print (Tech_languages[1]) # access the 2nd index
print ("************************************************************************************")

print (Tech_languages[1][2]) # access the 2nd index and 2nd element of the list
print ("************************************************************************************")
print ("\n")
print ("************************************Methods over the list*****************************************")


# insert the element to the list
# syntax for adding element to the list is --->list.append(element)
Backend_languages = []
Backend_languages.append("Python")
Backend_languages.append("Java")
Backend_languages.append("Ruby")
Backend_languages.append("C")
print (Backend_languages)
print ("*******************************inserting the element based on the position************************")

# syntax of inserting element in the list is ---> list.insert(position,element)
Backend_languages.insert(2,"C#")
print (Backend_languages)

print ("**************************extending the list with the 2nd list at end position********************")
# syntax for the extending list over the another list is ---> list1.extend(["elements"])
Backend_languages.extend(["R","IOT"])
print (Backend_languages)

print ("**********************************get the index value of the list*********************************")
# syntax for this is ---> list.index(element_name_in_the_list)

value = Backend_languages.index("R")
print (value)

print ("************************** delete the element fro the list********************")
print ("************************** 1)remove method ********************")
Backend_languages.remove("R")
print (Backend_languages)
print ("************************** 2) pop method********************")

list = [34,67,98,46]
list.pop()
print (list)

# pop the elements by index value
list.pop(1)
print (list)
print ("**************************Sorting the list********************")

# syntax of sorting list is ---> list.sort()

Backend_languages.sort()
print (Backend_languages)

print ("**************************Reversing the list********************")
# syntax for the reversing list is --->list.reverse()

Backend_languages.reverse()
print (Backend_languages)

print ("**************************functions over the list********************")
print ("**************************find length of the list********************")

# syntax for the finding the list ----> len(list)

length_of_list = len(Backend_languages)
print (length_of_list)

# to print both index value and element name in the list
# here enumerate() fun helps to get the both the values

for index_val,name_ele in enumerate(Backend_languages):
    print("index value is %s and element name is : %s" % (index_val,name_ele))