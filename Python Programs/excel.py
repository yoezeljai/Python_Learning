# script to work on excel
from openpyxl import load_workbook
from openpyxl import Workbook

print("complete")
myexcel=Workbook()      #create an excel workbook
mysheet=myexcel.active
mysheet['A1']='NAME'
mysheet['B1']='AGE'
mysheet['C1']='SALARY'
n=['A','B','C','D','E']
a=[25,26,27,28,22]
s=[45000,25000,20000,30000,12000]
rowscount=len(n)
startpos=2
listindex=0
while(rowscount!=0):
    namestr='A'+str(startpos)
    agestr='B'+str(startpos)
    salstr='C'+str(startpos)
    mysheet[namestr]=n[listindex]
    mysheet[agestr]=a[listindex]
    mysheet[salstr]=s[listindex]
    rowscount-=1
    startpos+=1
    listindex+=1
myexcel.save(r'/users/yoezeljai/desktop/test.xlsx')
