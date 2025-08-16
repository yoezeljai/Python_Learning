# Script to calcaute discount with if-elif-else statement

amt=int(input("Enter the amount:"))
if amt<=1000:
    disc=amt*0.05
    print("Discount is :" ,disc)
elif amt<=5000:
    disc=amt*0.10
    print("Discount is :",disc)
else:
    disc=amt*0.15
    print("Discount is:",disc)

print("Net Payable Amount is:",amt-disc)
