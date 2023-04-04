n=3
am=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    am.append(a)


print()
bm=am[:][:]

for i in range(len(am)):
    for j in range(len(am[0])):
        print(am[i][j],end=" ")
    print() 

print()
print()
print()

for i in range(len(am)):
    for j in range(len(am[0])):
        print(bm[j][i],end=" ")
    print()