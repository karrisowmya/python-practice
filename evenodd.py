#CHECK IF A NUMBER IS EVEN OR ODD:

num = int(input("enter num: "))
if(num%2==0):
    print(num,"is even")  #while using , space is by default added
else:
    print(num,"is odd")  

num = str(num)            #to use + we should first convert num to string and use +
print(num+" is number")   # space should be provided here