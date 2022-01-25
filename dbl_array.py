a=[1,2,3]
#print(a,a+a)
def dbl(a):
    n=len(a)
    res=[0]*2*n
    for i in range(n):
        res[i]=a[i]
        res[i+n]=a[i]
    return res
print(a,a+a,dbl(a))