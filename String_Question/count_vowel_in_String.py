a="How are You"
b=['a','e','i','o','u','A','E','I','O','U']
c=[]
c=dict(c)

for i in b:
    t=0
    if i in a:
            t=a.count(i)
            c[i]=t
print(c)
