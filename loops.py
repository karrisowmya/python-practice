#print nums from 1 to 100

i=1
while i<=100:
    print(i)
    i=i+1

#print nums from 100 to 1

i=100

while i>=1:
    print(i)
    i=i-1


#print multiplication table of a num

n=int(input("enter num: "))
i=1
while i<=10:
    print(n," * ",i," = ",n*i)
    i=i+1


#print elements of list

nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i=i+1


#search for a num in tuple using loops


tup=(1,2,3,4,5,6)
n=4
i=0
while i<len(tup):
    if(n==tup[i]):
        print("found")
    i=i+1


#break and continue keywords:

i=0
while i<=5:
    if(i==4):
        break
    print(i)
    i=i+1


i=0
while i<=5:
    if(i==3):
        i=i+1
        continue
    print(i)
    i=i+1


FOR LOOP:

nums=[1,2,3,4]
for i in nums:       #here i gets incremented by itself
    print(i)


name="sowmya"
for char in name:
    print(char)      #print individual characters
else:                #else is optional, it is used when we want to do some extra work after the looping statement
    print("all characters are printed")

name="sowmya"
for char in name:
    if(char=='m'):
        break
    print(char)
else:                  #else does not get executed when we use break, so else is used when u run total loop completely
    print("end")

n1 = [1,4,9,16,25,36,49,64,81,100]
for val in n1:
    print(val)

n2=(1,4,9,16,25,36,49,64,81,100)

x=25
idx=0

for el in n2:
    if(x==el):
        print(x," is found at idx ",idx)
        break
    idx=idx+1


#RANGE FUNCN IN FOR LOOP:  range(start?, stop, step?)

for el in range(5):
    print(el)              #o/p: 0 1 2 3 4

for el in range(1,5):
    print(el)                #o/p: 1 2 3 4

for el in range(1,5,2):
    print(el)                #o/p: 1 3


#PRINT NUMS FROM 1-100:

for el in range(1,101):
    print(el)

i=1
while(i<=100):
    print(i)
    i=i+1


#PRINT NUMS FROM 100-1:

for el in range(100,0,-1):
    print(el)

i=100
while(i>=1):
    print(i)
    i=i-1


#PRINT MULTIPLICATION OF A TABLE:

n = int(input())
for el in range(1,11):
    print(n*el)

#pass:

for el in range(5):          #IndentationError

print("end")


for el in range(5):           # to print the end without any errors we use pass, to pass the for block
    pass

print("end")


FOR AND WHILE LOOPS:

#PROGRAM TO FIND SUM OF FIRST N NUMBERS (while)

i=1
sum=0

while(i<=10):
    sum=sum+i
    i=i+1

print(sum)


#PROGRAM TO FIND FACTORIAL OF FIRST N NUMBERS(for)

n= int(input())
mul=1

for i in range(1,n):
    mul=mul*i
    print("factorial of ",i," is ",mul)