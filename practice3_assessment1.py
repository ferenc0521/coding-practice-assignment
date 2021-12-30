#zigzag 1 if subarray of length 3 is not monoton
#a<b>c or a>b<c
#[1,2,1,3,4]=>[1,1,0]
#1,2,1 =>1
#2,1,3 =>1
#1,3,4 =>0
#-----------------------------------------------------------
def solution(arr):
    res=[]
    for i in range(len(arr)-2):
        nonmon=(1 if (arr[i]>arr[i+1] and arr[i+1]<arr[i+2]) or (arr[i]<arr[i+1] and arr[i+1]>arr[i+2]) else 0)
        res.append(nonmon)
    return res
print (solution([1,2,1,3,4]))