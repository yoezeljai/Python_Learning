#Script for conditional statement example

a=int(input("Enter the Percentage marks:"))
if(a>=35 and a<50):
    print("3rd class")
elif(a>=50 and a<60):
    print("2nd Class")
elif(a>=60 and a<85):
    print("1st Class")
elif(a>=85 and a<100):
    print("Distinction")
elif(a>=100):
    print("Invalid")
else:
    print("FAIL")
