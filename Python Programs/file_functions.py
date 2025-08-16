#Script to demonstrate the file i/o functions and menthod

'''The below script open an existing jp.txt file in read mode and reads the
content of the file in 5 differnt ways using read(), readline() & readlines()'''

fobj=open('/users/yoezeljai/desktop/jp.txt','r') # opens a file named jp.txt in read mode
print('Name of the file is :',fobj.name)         # diplays the file name
print('Mode of the file is :',fobj.mode)         # displays the mode of the file
print(fobj.read())  #reads the content of the file till EOF as string
fobj.close()        #closes the file.

fobj=open('/users/yoezeljai/desktop/jp.txt','r')
print('Name of the file is :',fobj.name)
print(fobj.read(10),'\n')    #reads the content of the file till index 10
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp.txt','r')
print('Name of the file is :',fobj.name)
print(fobj.readline(),'\n')  #reads the first line of the file
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp.txt','r')
print("Name of the file is :",fobj.name)
print(fobj.readline(5),'\n') #reads the content of the file till index 5
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp.txt','r')
print('Name of the file is :',fobj.name)
print(fobj.readlines(),'\n') #reads the content of the file till EOF as list
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp.txt','r')
print('Name of the file is :', fobj.name)
print(fobj.readlines(18),'\n') #reade the content of the file at index 1
fobj.close()


'''The below script creates an file jp1.txt if the file doesn't exist and
 in write mode we will add new data/content to the file.'''

fobj=open('/users/yoezeljai/desktop/jp1.txt','w')   #opens a file in write mode
print("Name of the file is :",fobj.name)
print('Mode of the file is :',fobj.mode)
data="this is write method"     #data which has to be added to the file as string
fobj.write(data)                #this method writes the data to the file
print("the data has been written on the file\n")
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp1.txt','w')   
print('Name of the file is :',fobj.name)
print('Mode of the file is :',fobj.mode)
data=['jp\n','ic\n']
fobj.writelines(data)           #This menthod write data as list to the file.
fobj.close()
print('\n')

'''The below script creates an file jp1.tzt , if the file doesn't exixt and in
append mode ,use read and write method to add new data/content to the file with existing data'''

fobj=open('/users/yoezeljai/desktop/jp1.txt','a')
print('Name of the file is :',fobj.name)
print('Mode of the file is :',fobj.mode)
data=['this is new append mode\n','this is python\n']
fobj.writelines(data)
print('New data has been appended\n')
fobj.close()

fobj=open('/users/yoezeljai/desktop/jp1.txt','r')
print(fobj.readlines())
fobj.close()
