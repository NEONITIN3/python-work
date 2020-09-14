##square
c=[i**2 for i in range(1,9)]
print(c)

c=[pow(i,3) for i in range(1,9)]
print(c)

m=["is even" if i%2==0 else  "is odd" for i in range(10) ]
print(m)
