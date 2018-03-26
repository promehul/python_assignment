
str = raw_input("Enter a string")
c1 = 0;c2 = 0; c3 = 0;
re = ""
for i in range(0,len(str)):
  if(str[i] == "."):
    re+=". " 
    c2=1
    c1=1
    
  elif(str[i] != " " and  str[i] != "."):
    c3 = 1
    c1= 0
    re+=str[i]
  else:
    if(c2==0 and c3==0):
      #don't do anything
      continue
    
    if(c1 == 0):
      re += str[i]
      c1 = 1
    

print re
