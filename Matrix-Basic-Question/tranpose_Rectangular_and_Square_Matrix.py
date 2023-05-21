# transpose matrix
print("\n\nSQUARE MATRIX")

am=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(am)):
    for j in range(len(am)):
        print(am[j][i],end=" ")
    print()

print("\n\nRECTANGULAR MATRIX")
bm=[[1,2],[3,4],[5,6]]
#rectangular Matrix
for i in range(len(bm[0])):
    for j in range(len(bm)):
        print(bm[j][i],end=" ")
    print()
