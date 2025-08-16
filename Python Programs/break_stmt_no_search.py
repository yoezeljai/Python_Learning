# Script to scearch a number from a list and demonstrating break statement if number if found
no=int(input("Enter the number:"))
numbers=[11,22,33,44,55,66,77]
for num in numbers:
    if num==no:
        print("number found in list")
        break
    else:
        print("number is not found in the list")
