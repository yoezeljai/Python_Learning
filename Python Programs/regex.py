# script for regular expressions
import re
var='today we have python class python is easy i like python'
res1=re.match('python',var)         #checks only for the first word in var
res2=re.search('python',var)]       #checks for the first intance in var
res3=re.findall('python',var)       #checks all the intance of sub-string
res4=re.sub('python','java',var)    #replaced all the sub-string with new sub-string
print(res)
print(var)
#print(res.group())
