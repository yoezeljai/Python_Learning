# Count and print the content within <html> </html> from thr below snippet.
StartPos=0
StartPos1=0
var="""line1
line2
<html>
 line3
</html>
line4
line5
line6	
<html>
 line7
 line8
</html>
 line9
 line10
<html>
 line11
 line12
 line13
</html>"""
cnt=var.count("<html>")
print("Count is:",cnt)
while(cnt>0):
    pos=var.index("<html>",StartPos,len(var))
    pos1=var.index("</html>",StartPos1,len(var))
    if(var.startswith("<html>",pos,len(var)) & var.endswith("</html>",pos1,len(var))):
       print(var[pos+6:pos1])
    print("Position is:",pos)
    print("Position is:",pos1)
    cnt-=1
    StartPos=pos+1
    StartPos1=pos1+1


    
        
