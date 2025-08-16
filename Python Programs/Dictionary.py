# Script for create ,access ,update and delete and dictionary
dic={'name':'jp','age':'28','city':'blr'} # created and dict with key:value
print('Dictionary content is :',dic)    #displayes the dict contents
print('Name is:',dic['name'])   #access the dict value with key
print('Age is:',dic['age'])

dic['age']=29       #updated the key age with new value
print('New age is:',dic['age'])

dic['zip']=560078   # added new key with value to the dict
print('New key zip is:',dic['zip'])

print('updated dictionaly contents are:',dic)   #displays the new dict data

del dic['zip']      #deletes the key zip with its value
print('Dictionary content is :',dic)

dic.clear()     #removes all the entires in the dict
print('Dictionary content is:',dic)

del dic         #detetes the entire dictionary
print('Dictionary content is:',dic) #this state will throw an error as dic do not exist
