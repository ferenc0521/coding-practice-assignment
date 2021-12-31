'''
practice 4 assessment 2
array of non negative integers numbers return true if it is strictly increasing allowing at most one swap operation, swapping any two digits in the number 
leading zeroes ommitted
[1,5,10,20] => True (no swap needed)
[1,3,900,10] => True (900 - 009 - 9)
[1,3,800,900,10] => False (two swaps needed)
'''
def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
def swaps (n):
    swaps=[]
    digits=str(n)
    if len(digits) == 1 :
        swaps=[n]
        return swaps
    for i in range(len(digits)-1):
            for j in range(i+1,len(digits)):
                #print(digits,digits[i],digits[j])
                num=int(swap(digits,i,j))
                swaps.append(num)
    #print(swaps)
    return swaps
def fixable (l,m,r):
    mswaps = swaps(m)
    rswaps = swaps(r)
    for n in mswaps:
        if l<n and n< r:
            return True
    for n in rswaps:
        if l<m and m<n:
            return True
    return False
def solution(a):
    problems=0
    fixes=0
    al=len(a)
    for i in range(al-1):
        if i>0 :
            if a[i-1] < a[i] and a[i] < a[i+1]:
                continue
            else:
                if fixes==0 and fixable(a[i-1], a[i], a[i+1]):
                    fixes += 1
                    continue
                else:
                    problems += 1
                    break
        else:
            if a[i] < a[i+1]:
                continue
            else:
                if fixable(-1, a[i] , a[i+1]):
                    fixes += 1
                    continue
                else:
                    problems += 1
                    break
    if problems < 1 :
        return True
    else:
        return False    

print ( [1,5,10,20], solution([1,5,10,20]) )        #True
print ( [20,10,5,1], solution([20,10,5,1]) )        #False
print ( [1,3,900,10], solution([1,3,900,10]) )       #True
print ( [1,3,800,900,10], solution([1,3,800,900,10]) )     #False