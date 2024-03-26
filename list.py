#LISTS:


#SORT LIST:

list = ["a","d","g","w"]
print(list.sort())   #None
list.sort()
print(list)          #['a','d','g','w']


#METHODS IN LIST:

movies=[]
m1=input()
m2=input()
m3=input()
movies.append(m1)
movies.append(m2)
movies.append(m3)
#movies.append(m1,m2,m3) error: list.append() takes exactly one argument
print(movies)


m=input()
movies.append(m)
m=input()
movies.append(m)
m=input()
movies.append(m)
print(movies)

or

movies.append(input())
movies.append(input())
movies.append(input())
print(movies)