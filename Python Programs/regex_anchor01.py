#
import re
var=''' INDIA ip 1.1.1.1
USA ip is 162.12.1.144
UK ip is 111.142.113.2
AUSTRALIA ip is 12.14.16.1115 '''
cnt=re.findall('[A-Z]{2,}',var)
print(cnt)
ip=re.findall('[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}',var)
print(ip)

var1=''' My dob is 01.12.1966 and
my friends  dob is 12/08/1977 and
My sisters dob is 03:02:1987 and
my son's dob is 24@01@2015'''
dob=re.findall('[0-9]{2}[./:@][0-9]{2}[./:@][0-9]{4}',var1)
print(dob)               
res=re.sub('[0-9]{2}[./:@][0-9]{2}[./:@][0-9]{4}','DDMMYY',var1)
print(res)
res1=re.sub(' ','',var1)
print(res1)

var3='''My email id is sam@gmail.com
My email id is jp@yahoo.com
My frnds email id is sky147@rediff.com'''
em=re.findall('[a-zA-Z0-9]{1,}[@][a-zA-Z]{1,}.com',var3)
print(em)

