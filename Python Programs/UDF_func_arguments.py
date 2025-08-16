#Script for FUNCTION ARGUMENT
def add(x,y):       # Required argument
    z=x+y
    return z
def emp(name,age):  # Keyword argument
    print('Name is :',name)
    print('Age is :',age)
    return
def addy(city,state,country='INDIA'):    #Default argument
    print('City is :',city)
    print('State is :',state)
    print('Country is :',country)
    return
def no_list(val , *val1):           #variable length Argument
    print(val)
    print(val1)
    return
