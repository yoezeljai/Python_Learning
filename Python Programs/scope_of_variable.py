#Script to display scope of a variable
total=0     #Global variable
def sum(a,b):
    total=a+b   # here total is local to this function
    return total

print(total)
op=sum(20,10)
print(op)
