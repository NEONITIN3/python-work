#seperate the list value from max 45 and min 45

l=[12,34,55,67,89,34,40,44,62,79,100,1,3,59]
maxlist=[]
minlist=[]
[
maxlist.append(x)
if x>=45 else minlist.append(x)
for x in l
]
print (minlist)
print(maxlist)

