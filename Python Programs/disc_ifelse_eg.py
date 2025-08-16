# Script to calculate discount

amt=int(input("Enter the amount:"))
if(amt<10000):
    disc=amt*0.05
    print("Discount is:",disc)
else:
    disc=amt*0.10
    print("Discount is :",disc)

print("Net payable is:" ,amt-disc)
