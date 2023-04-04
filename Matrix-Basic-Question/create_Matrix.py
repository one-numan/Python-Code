print("\n\n")

print("Create Martix Enter the length of N for NXN Martix")
n=int(input("Enter :"))
matrix=[]
for i in range(n): #row enteries
    a=[]
    for j in range(n):#column enteries
        print("Enter A[ ",i,j," ]  :",end="")
        
        a.append(int(input()))
    matrix.append(a)

print()
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()

