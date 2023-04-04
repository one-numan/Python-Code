n=int(input("Enter the Length of the matrix"))
# matrix multiplication
am=[]
bm=cm=[]
for i in range(n):
    a=[]
    c=[]
    for j in range(n):
        a.append(int(input()))
        c.append(0)
    am.append(a)
    cm.append(c)

for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input()))
    bm.append(b)

for i in range(len(am)):
    for j in range(len(bm[0])):
        for k in range(len(cm)):
            cm[i][j]+=am[i][k]*bm[k][j]
        

for i in range(n):
    for j in range(n):
        print(cm[i][j],end="")
    print()

