#Script for nested if statement

num=int(input("Enter the number:"))

if num%2==0:
    if num%3==0:
        print("Divisible by 3 and 2")
    else:
        print("Divisible by 2 but not by 3")
else:
    if num%3==0:
        print("divisible by 3 but not 2")
    else:
        print("Not divisible by 2 or 3")

    
