n=int(input("enter a no."))
a=[0,1]

[a.append(a[x-2]+a[x-1]) for x in range(2,n)]

print(a)

for i in range(0,n):
  print(a[i]**3)
