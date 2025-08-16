#Script for file handling
fvar=open(r'/users/yoezeljai/desktop/file.txt','r')
data=fvar.read()       # returns the file in string format
   # returns the file in list format

print(data)
print("\n")
print('Count of txt(INDIA): ',data.count('INDIA'))  # Counts the occurance of sub-string
print('\n')
print(data.replace('INDIA','BHARAT'))               # Replaced the sub-string with new value
print(type(data))
data1=fvar.readlines()
print(data1)
fvar.close()
