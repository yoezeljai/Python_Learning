#

def genex(x,y):
    res1=x+y
    yield res1
    res2=x-y
    yield res2
    res3=x*y
    yield res3
op=genex(40,20)
print(list(op))
'''print(op)
print(next(op))
print(next(op))
print(next(op))
print(next(op))'''
