#Script for regular expression with pattern anchor
import re
var='my mobile no is 1234567890 & 2345678901 & 9876543211'
res=re.findall(' [0-9]{10} ',var)
print(res)

