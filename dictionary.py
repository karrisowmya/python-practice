#DICTIONARIES:

dict={
    "name":"sowmya",
    "age":20,
    "marks":[12,14,17]
}
print(dict)
print(dict["name"])
dict["name"]="triveni"
print(dict)



vocabulary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}
print(vocabulary)


#to take marks of 3 subjects from user and store it in dictionary

marks={}
a=float(input("enter phy: "))
marks.update({"phy":a})

b=float(input("enter chem: "))
marks.update({"chem":b})

c=float(input("enter soc: "))
marks.update({"soc":c})
print(marks)



#NESTED DICTIONARY:


student={
    "name":"sowmya",
    "marks":{
        "c":84,
        "java":94,
        "python":93
    },
    "branch":"cse"
}
print(student)                  #to print the dictionary
print(student["marks"])         #to print value of a specific key
#print(student["age"])          #gives error as key age does not exist in dictionary
print(student["marks"]["c"])    #to print value of a nested dictionary
print(student.keys())           #to print all keys of dictionary
print(list(student.keys()))     #to print keys in the form as list
print(student.values())         #to print all the values of dictionary
print(list(student.values()))   #to print values in the form of list
print(tuple(student.values()))  #to print values in the form of tuple
print(student.items())          #to print (key,value) pairs as tuple
print(list(student.items()))    #to print key,value pairs in the form of list
print(tuple(student.items()))   #to print key,value pairs in the form of tuple
print(student.get("name"))      #to print value of specific key
#print(student.get("age"))      #returns None if key not exist in dictionary
student["age"]=20               #to assign new key,value into dictionary
print(student)

dict={"year":"3rd","roll no":318}
student.update(dict)
print(student)