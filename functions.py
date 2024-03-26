# TO ADD TWO NUMBERS

def calc_sum(a,b):
    sum = a+b
    print(sum)


calc_sum(2,5)
calc_sum(4,2)
calc_sum(48,3)

#OR

def calc_sum(a,b):
    sum=a+b
    return sum

print(calc_sum(2,6))
print(calc_sum(58,28))

#AVERAGE OF 3 NUMBERS

def avg_nums(a,b,c):
    avg=(a+b+c)/3
    return avg

print(avg_nums(2,4,6))
print(avg_nums(4,2,9))

#OR

def avg_nums(a,b,c):
    avg=(a+b+c)/3
    print(avg)

avg_nums(2,4,6)
avg_nums(4,2,9)


#DEFAULT PARAMETERS

# def prod(a,b):
#     return a*b

# prod()

def prod(a=2,b=5):
    print(a*b)

prod()

#OR

def prod(a,b=5):
    return a*b

print(prod(2))


#PRINT LENGTH OF THE LIST

def len_list(l):
    le=len(l)
    print(le)
    print(l)

#TO PRINT ELEMENTS OF LIST IN SAME LINE

def print_list(l):
    for i in l:
        print(i,end=" ")       #print is a built-in func, to print elements in same line we use end

list1=[2,5,3,6]
len_list(list1)
print_list(list1)
list2=["sowmya",90]
len_list(list2)
print_list(list2)



#FACTORIAL OF A NUM


def facto(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    return f                 #if return f is not used then o/p is None

print(facto(3))


#CONVERT DOLLAR TO RUPEES

def con_rup(d):
    rs= 83.43*d
    #return rs
    #print(rs)                     #834.3000000000001
    rounded = round(rs)            #834
    print(rounded)

# print(con_rup(10))               #834.3000000000001

con_rup(10)