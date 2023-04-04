n=int(input("Enter the Length of the Matrix"))
ma=[] #matrix A
mb=[] #matrix B


mac=[]

for i in range(n):
    c=[]
    a=[]
    for j in range(n):
        a.append(int(input( )))
        c.append(0)
    ma.append(a)
    mac.append(c)



for i in range(n):
    for j in range(n):
        print(ma[i][j],end=" ")
    print()

print("Your B")


for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(input()))
    mb.append(b)


print("Your NEW  Matrix")
for i in range(len(ma)):
    # c=[]
    for j in range(len(ma[0])):
        # for k in range(len(mac)):
            mac[i][j]=ma[i][j] + mb[i][j]
            print(ma[0])
        



for i in range(n):
    for j in range(n):
        print(mac[i][j],end=" ")
    print()



