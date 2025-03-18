#Dictionaries are used to store data values in (Key:value) pairs    Eg: Words and Meanings in an english dictionary     In pairs
#Unordered(no index), mutable(changable) and don't allow duplicate keys  
#Also a list and a dictionary cannot be a key since it's value is mutable. However, a value can be anything.   
#A key should be kind of value which is not mutable. therfore we avoid using list and dictionary as key
#dict["Name"], dict["Age"], dict["Money"] -- to access the key     #dict["Key"] = "value" -- to assign or add new value to an existing word in dictionary
dict = {
    "Name" : "Javed",
    "Age"  : 24,
    "Money": 99.99,

}
print(dict)

info = {
    "key" : "value",
    "name" : "Javed",
    "age" : "27",
    "is adult" : True,
    "Money"  : 99.9,
    "Subjects" : ["C", "Python"],
    "Topics"   : ( "dict", "set"),
    12.99 : 90.7,
    }
print(type(info))
print(info["name"])
info["name"] = "Sahil"         #replaced from Javed to Sahil_Khan
info["surname"] = "khan"
print(info)

#null dictionary (initially empty but gradually we add values)
null_dict = {}
null_dict["name"] = "Ayaan_Khan"
print(null_dict)

#Nested Dictionary
student = {
    "name" : "Javed_Khan",
    "subjects" : {                  #could have used a list if we only wanted to input subjects. But for subjects with marks we use nested dictionary.
        "Python" :  87,
        "English" : 90,
        "AM" :  75,
    } 
}
print(student)                              #printing complete contents of the dictionary
print(student["subjects"])                  #extracting subjects from the dictionary
print(student["subjects"]["Python"])        #Extracting relevant information from the nested dictionary
print(student.keys())                       #Nested keys are not extracted. just prints the outer keys
print(list(student.keys()))                 #prints the result as a list            basically removes dict_keys from the o/p
print(len(student))                         #for the number of key value pairs
print(len(list(student.keys())))            #for the number of key value pairs
print(student.values())                     #returns all the values in dictionary
print(list(student.values()))               #conversion from value to a list        basically removes dict_values from the o/p
print(student.items())                      #prints all combinations as key,val pairs
print(list(student.items()))                #o/p as a list
pairs = list(student.items())
print(pairs[0])                             #accessing a particular pair from the o/p based on index
#print(student["name2"])                    #gives an error since it doesn't exist. will also stop the execution of further code therefore we use method approach
print(student.get("name2"))                 #gives no error #Method approach. Doesn't give an error but instead returns none.
student.update({"city" : "Delhi"})
print(student)

new_dict = {"Age" : 18, "Domicile" : "U.P"}     #ALternate way of adding new key and values to a dictionary
student.update(new_dict)
print(student)

#new_dict = {"name" : "Ayaan", "Age" : 15}
#student.update(new_dict)                       #this won't create a new key rather replace the contents of old one (no duplicacy allowed in Dictionary) 

#Dictionary Methods
""" myDict.keys()                   #returns all keys
    myDict.values()                 #returns all values
    myDict.items()                  #returns all (key,val) pairs as tuples
    myDict.get("key")               #return the key according to the value
    myDict.update(newDict)          #inserts specified items into the dictionary
"""

#Set is a collection of unordered items. Each item must be unique and immutable
#We can store int,float,string,tuple and boolean in a set but not lists and dictionary since they are mutable

set12 = {1,2,3,"Hello", 9.99, "Hello"}      #Duplicates values ignored without error in the terminal
print(set12)
print(type(set12))
print(len(set12))

#for creating an empty set we cannot just write set12 = {} (this is a dictionary), rather we write set12 = set() for an empty set

#Set Methods
"""set.add(element)         #adds an element
   set.remove(element)      #removes an element
   set.clear()              #empties the set
   set.pop()                #removes a random value
"""
#Sets themselves are mutable however the elements in them are immutable

collection = set()                                      #Hashable -- Immutable  (a restricted and fixed hash value)
collection.add(1)                                       #unhashable -- mutable  (an unrestrictive and variable hash value) --- Dicitonary, List, sets
collection.add(5)
collection.add(5)
collection.remove(1)
collection.add ("Javed_khan")
print(collection)

collection.clear()                              #Clears the set
print(len(collection))

collection2 = {1,2,3,"Hello", 9.99, "Hello"}
print(collection2.pop())                        #random elements pop from the set
print(collection2.pop())                        #picks another random element

#Union and intersection in sets         Eg: set1.union(set2)    set1.intersection(set2)

#WAP to store words and meanings provided in python dictionary
dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat"  : "a small animal",
}
print(dict)

#WAP given list of subjects for studnets. 1 classroom req for 1 subject. how many classrooms for all students 
set = {"Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"}
print("Number of classrooms required: ", len(set))

#WAP to enter marks of 3 subj from user and store in dict. Start empty and add one by one.
null_dict = {}
sub1 = input("Enter the first subject: ")
mark1 = int(input("Enter the marks of first student: "))
null_dict.update({sub1 : mark1})
sub2 = input("Enter the second subject: ")
mark2 = int(input("Enter the marks of second student: "))
null_dict.update({sub2 : mark2})
sub3 = input("Enter the third subject: ")
mark3 = int(input("Enter the marks of third student: "))
null_dict.update({sub3 : mark3})
print(null_dict)

#WAP to figure out a way to store 9 and 9.0 as seperate values in a set
set1 = {9,9.0,8,8.0}            
print(set1)

set2 = {9, "9.0"}       #considering one of them as strings
print(set2)

set3 = {
    ("float", 9.0)
    ("int", 9)
}
print(set3)

#05:00:00
