#TUPLES:

#tuples are immutable
tup=(1,2,3,4,5)
print(type(tup))
print(tup[0])
print(tup)
#tup[0]=7       error: tup object does not support item assignment
print(tup[1:4]) #(2,3,4)
print(tup[:4])  #(1,2,3,4)
print(tup[0:])  #(1,2,3,4,5)
print(tup.index(2)) #print's index of value 2 which is 1
print(tup.count(4)) #print's how many times 4 is exist in tuple

tup1=()         #output: ()
print(tup1)

tup2=(1,)       #to print a single values tuple we should separate it with a comma
print(tup2)     #(1,)

#if single values tuple is not separated by comma then it's type becomes int
tup3=(2)
print(tup3)     #2
print(type(tup3))  #int


#TUPLE COUNT:

tuple=("a","b","c","a","d")
print(tuple.count("a"))

#   there is no sort method in tuples to sort we should use list