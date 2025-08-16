# Script for number guessing game

MyNum= 3
x=0
count=0
while(x==0):
    a=int(input("Guess the number:"))
    count+=1
    if(a==MyNum):
        print("congrats you have guess it correctly")
        print("Total attempts to guess are:" ,count)
        break
    else:
        print("sorry try again")

