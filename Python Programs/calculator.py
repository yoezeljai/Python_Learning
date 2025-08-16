#Script for calculator
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=input("What function to perform (add,sub,mul,div):")
if(c=="add"):
    res=a+b
    print(res)
if(c=="sub"):
    res=a-b
    print(res)
if(c=="mul"):
    res=a*b
    print(res)
if(c=="div"):
   res=a/b
   print(res)
else:
    print("Not a valid function")



