print "This is a program to find all the integer coordinates between a given range"

x = int(raw_input("Enter the first no.="))
y = int(raw_input("Enter the second no.="))
z = int(raw_input("Enter the third no.="))
n = int(raw_input("Enter the integer N.="))


def check(x,y,z):
  coord = []
  coord =  [(i,j,k) for i in range(0,(x+1)) for j in range(0,(y+1)) for k in range(0,(z+1)) if((i+j+k)!=n)] 
  return coord

coordi = check(x,y,z)
print coordi
