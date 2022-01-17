"""
Array

Arrays are basically lists, in which you can define different types of variables in each of
 the cells, adding and removing cells.
To define an array wrap it with square brackets.
"""
arr1 = [5, 20, 44, 2] #each cell is seperated by commas.
print(arr1) #To display the entire content of the array simply send it to print

"""
To access a single cell you can access the array by the index in the list inside
of square brackets, starting with 0.
"""
print(arr1[0]) #Displays 5
print(arr1[2]) #Displays the value of the third cell

"""
Objects

Objects are key:value dictionaries. In each key you can define any of the python types as its value.
To define an object wrap it around curly braces.
"""

obj1 = {
    "key1": 5, #To add another key:value seperate it by commas.
    "key2": "Hello",
    "key3": True,
    "key4": [1, 1, 2, 3, 5, 8],
}
print(obj1) #The display all the contents of the object simply send it to print

"""
To access a single key's value you can use square brackets with the key as string
"""
print(obj1["key1"])