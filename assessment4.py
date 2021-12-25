# ribbon cutting a[i] length of the ribbon k ribbons of the same lengths 
# into cutting the ribbons as many pieces as you want
# max integer length L for which it is possible to obtain  
# at least k ribbons of length L by cutting the given ones
# a=[5,2,7,4,9] and k=5  solution a,k =>4
def solution(a,k):
    for l in range(1,max(a)):
        n = map(lambda x: int(x/l) , a)
        if sum(n) < k:
            break
    return l-1
print solution( [5,2,7,4,9] , 5 )
print solution( [5,2,7,4,9,10] , 5 )
print solution( [5,2,7,4,9] , 4 )