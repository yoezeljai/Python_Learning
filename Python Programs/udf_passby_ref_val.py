#Script to demonstrate pass by reference and pass by value
def add(x,y):
    z=x+y
    print('Sum of x & y:',z) # pass by reference    
    x,y=10,20
    print('new sum is :',x+y) #pass by value
