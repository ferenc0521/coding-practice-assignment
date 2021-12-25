n=5 
a=[4,0,1,-2,3] #=> b=[4,5,-1,2,1]
#b[i]= a[i] + a[i+1] (or 0) + a[i-1] (or 0)
def solution(a,n): #s.sort() could be used if we don't mind the in-place sorting
    b=[]
    for i in range(0,n):
        b.append(a[i] + (a[i-1] if i>0 else 0) + (a[i+1] if i< (n-1) else 0) )
    return b
print solution(a,n)
