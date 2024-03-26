#SETS:

set1={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(set1))

#store 9 and 9.0 in a set

set={9,9.0}
print(set)    #{9}

set1={9,"9.0"}
print(set1)

set2={"9",9.0}
print(set2)

values={
    (9.0,9)
}
print(values)


#SETS METHODS:

set1={1}               #to define empty set:  set1=set()

set1.add(2)
set1.add(2)
set1.add("sowmya")
set1.add((1,2,3))
print(set1)
print(len(set1))
print(type(set1))

set1.remove(1)
print(set1)

#set1.remove(8)   #when we try to remove ele which is not present in set then error occur  KeyErrror:8

#set1.clear()
#print(len(set1))

print(set1.pop())
print(set1)


set2={1,2,3}
set3={3,4,5}
print(set2.union(set3))         #{1,2,3,4,5}

print(set2.intersection(set3))  #{3}