#max frequencies 0/300
#solution(arr,m)
#return int array r with the maximum frequencies in each of the contiguous subarray of length m
def solution(arr,m):
    res=[]
    l=len(arr)
    print "-"
    if m<=l :
        for i in range(l-m):
            s=arr[i:i+m]
            max_freq=0
            for j in range(len(s)):
                occ=map(lambda x: 1 if x==s[j] else 0,s)
                freq=sum(occ)
                max_freq=max(freq,max_freq)
                print 'j=',j,'s[j]=',s[j],'freq=',freq,'max_freq=',max_freq,'s=',s
            res.append(max_freq)    
            print 'i=',i,'subarray_length=',l-m,'array=',arr,'subarray=s',s,'res=',res
    return res
print solution([1,2,3,4,4,5,5,5,5],4)