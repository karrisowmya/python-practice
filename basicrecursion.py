BASIC RECURSION FUNCTION:

def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

show(5)


FACTORIAL OF A NUMBER:

def facto(n):
    if(n==0 or n==1):
        return 1
    return n*facto(n-1)

print(facto(5))


SUM OF FIRST N NATURAL NUMBERS:

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n

print(sum(5))


PRINT ALL THE ELEMENTS IN THE LIST:

def lis(lis1,n=0):
    l=len(lis1)
    if(n==l):
        return 0
    print(lis1[n])
    lis(lis1,n+1)

list1=[1,2,3,4,5]
lis(list1)
