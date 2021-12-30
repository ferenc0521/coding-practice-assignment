'''
count contiguous subarrays with strictly decreasing sequence
[9,8,7,6,5]=>15
5+4+3+2+1
[10,10,10]=>3
'''
def monoton(arr):
    m=[]
    for i in range(len(arr)-1):
        #print(i,arr[i] , arr[i+1],arr[i] > arr[i+1])
        if arr[i] > arr[i+1]:
            m.append(1)
        else:
            m.append(0)
    #print (arr,m,sum(m),sum(m)==len(m))
    if sum(m)==len(arr)-1 :
        return True
    else:
        return False
def solution(arr):
    res=0
    al=len(arr)
    for i in range(al):
        for j in range(al-i):
            #print("monoton?",arr,res,i,j,arr[i:i+j+1], monoton(arr[i:i+j+1]))
            if monoton(arr[i:i+j+1]):
                res = res+1 
    #print("****result",res)
    return res
print([9,8,7,6,5],solution([9,8,7,6,5]))
print([10,10,10],solution([10,10,10]))