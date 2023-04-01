# Code Is Incomplete


def rev_a(a):
    if len(a) == 1:
        return a[0]
    else:
        pass
        return rev_a(a[:-1])

a=[11,22,33,44]
b=rev_a(a)
print(b)

