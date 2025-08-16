class B:
    'this class is B class'
    refno=15732
    def __init__(self,accno):
        self.eaccno=accno
        print(self.eaccno)
    def test1(a,b):
        res=a-b
        return res
    def displayaccno(self):
        return self.eaccno
    def B1(p):
        return p.strip()
    def B2(m):
        return m.split()

class A(B):
    'this class is A class'
    count=0
    def super__init__(self,name,age,sal):
        self.ename=name
        self.eage=age
        self.esal=sal
        print("Inside init\n")
        print(self.ename,self.eage,self.esal)
        A.count+=1
    def _displaysal(self):      #this will be hidden to outside class.
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

obj4=B(1244)
obj1=A(2000,2)

op=A.B1("     jp   ")
print(op)

op1=A.test1(40,20)      # Function over-writing
print(op1)

op2=B.test1(40,20)      # Function Over-loading
print(op2)

op3=obj1._displaysal()
print(op3)
