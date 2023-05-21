def add(**args):
    sum=0
    for i,y in args.getvalues():
        sum=sum+i
    print(type(args))
    
    return args

# a=(12,3,4,556,66)
print(add(a=12,b=12,c=12,d=43,e=123))
