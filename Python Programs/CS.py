#Script for nested if statement
a=25
if(a>20):
   print(" a is greater")  
   if(a%2==0):                      #will return remainder
       print("a is even number")
   else:
        print("a is odd number")
else:
    print("a is lesser")
