#IF ELSE:


age = int(input("enter your age: "))
if(age>18):
    print("right to vote")
else: 
    print("cant vote")

marks = float(input("enter marks: "))
if(marks>=90):
    print("A")
elif(marks>90 and marks<=80):
    print("B")
elif(marks>80 and marks<=70):
    print("C")
else:
    print("D")