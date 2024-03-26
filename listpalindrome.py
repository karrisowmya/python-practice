#CHECK IF A LIST IS PALINDROME OR NOT

list=[1,2,3]
list2=list.copy()
list2.reverse()
if(list==list2):
    print("palindrome")
else:
    print("not palindrome")