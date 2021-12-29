#solution(arr,l,r) 100/300
#return boolean array r
#r if there is integer x where arr[i]=(i+1) * x , and l <= x <= r
#forgot to check for arr[i]/(i+1) = int(arr[i]/(i+1))
def solution(arr,l,r):
    res=[]
    for i in range(len(arr)):
        x=1.0*arr[i]/(i+1)
        res.append( int(x) == x and l<=x and x<=r)
        print 'i=',i,'a[i]=',arr[i],'x=',x,'intx=',int(x), 'int?',int(x) == x,l,'<=',l<=x,r,'>=',x<=r,'res=',(int(x) == x and l<=x and x<=r)
    return res
print [3,3,1,4,3,4,5,16,32],2,48,solution([3,3,1,4,3,4,5,16,32],2,48)