print "This is a program to find all the prime numbers between a given range"

a = int(raw_input("Enter the first no."))
b = int(raw_input("Enter the second no."))
primes = []
for x in range(a,(b+1)):
  count = 0;
  for i in range(2,x):
    if(x%i==0):
      count = count +1      
  if(count==0):
    primes.append(x)

print (primes)
