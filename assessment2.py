a1= [1,3,5,6,4,2] #=> b=[1,2,3,4,5,6] return true strict ascending order
a2= [1,4,5,6,3]   #=> b=[1,3,4,6,5] return false 
def solution(a): 
    al=len(a)
    b=[]
    c= al/2 if al % 2 == 0 else int(al/2)+1
    strct=True
    for i in range(0,c):
        b.append(a[i])
        if i < al-i-1:
            b.append(a[al-1-i])
    for i in range(0,len(b)-1):
        if b[i]>=b[i+1]:
            strct=False
            break
    return strct
print solution(a1)
print solution(a2)
