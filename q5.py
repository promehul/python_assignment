pyList = ['mix', 'xyz', 'apple', 'xanadu', 'aardvarrk']
c=0 
d=[]
e=[]
for x in range(0,len(pyList)):
   
    if(pyList[x][0]=='x'):
       d.append(pyList[x])
        
    else:
       e.append(pyList[x])    
       
    
d=sorted(d)

e=sorted(e)

print(d+e)
