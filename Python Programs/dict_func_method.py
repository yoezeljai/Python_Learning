#Script for functions & Methods of dictionary

dic={'name':'jp','age':28,'city':'blr'}     # created an dic with key:values
print('Dictionary content is:',dic)         # print the content of dict

print('length of dic is:',len(dic))     # will return the length of dic

print('String representation of dic:',str(dic)) # printable string representation of dict

print('Type of variable dic is:',type(dic))     # will return the what type of var is dic

dic1=dic.copy()     #copies all the elements from dic to dic1
print('Content of dic1 is:',dic1)

print('country is:',dic.get('country','IND')) #as country is not present it will return IND as it value

print('Values:',dic.items())        #returns the list of tuple pairs

print('Keys in dic are:',dic.keys())    # prints all the keys in dict dic

print('Age is:',dic.setdefault('age','none'))
print('Country is :',dic.setdefault('country','IND')) #sets the default value of the key
print('Dictionary content is:',dic)     #displays the new key country along with old keys

dic2={'zip':560078}
dic.update(dic2)        #updates the dic2 key:values to dic
print('Dictionary content is:',dic) #displays the dic and dic2 key:values as one dic

print('Values of dic:',dic.values())    #returns the list of all the values in dic

dic.clear()           #removes all the items from the dictionary
print('the content of dic is cleared')
print('Content of dic is:',dic)     # diplays a empty dictionary
