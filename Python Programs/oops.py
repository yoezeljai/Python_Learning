# 
class A:
    'this class is a test class'
    count=0
    def __init__(self,name,age,sal):
        self.ename=name
        self.eage=age
        self.esal=sal
        print("Inside init\n")
        print(self.ename,self.eage,self.esal)
        A.count+=1
    def displaysal(self):
        return self.esal
    def test1(x,y):
        res=x+y
        return res
    def incrementsal(self,new):
        self.newsal=new
        self.esal=self.esal+self.newsal
        return self.esal
    def test2(x):
        return x.upper()

print(A.__doc__)                #this will print the class doc
print(A.__dict__)               #this will print all the function under the class
print(A.__name__)               #this will print the name of the class

obj1=A('sam',33,25000)
obj2=A('tan',32,50000)
obj3=A('jai',33,70000)

print(obj1.esal)
a=getattr(obj1,'esa','novalue')     #this will check for variable in the class
print(a)

b=hasattr(obj2,'ename''novalue')    #this will 
print(b)

print(obj1.esal)
print(obj2.eage)
print(obj3.esal)
op=obj2.displaysal()        #Object method
print(op)
op1=A.test1(20,10)          #class method
print(op1)

op2=obj1.incrementsal(60000)
print(op2)
op3=A.incrementsal(obj1,60000)
print(op3)
op4=A.displaysal(obj1)
print(op4)
