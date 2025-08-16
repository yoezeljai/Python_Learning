# Script to count the sub-string
StartPos=0
var="hi sam hello sam by sam good sam bad sam"
res1=var.count("sam")
print("count is :",res1)
while (res1>0):
    res=var.index("sam",StartPos,len(var))
    print("Position of sam is:",res)
    StartPos=res+1
    res1-=1
