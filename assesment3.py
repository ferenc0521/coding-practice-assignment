# "99" "99" = "1818"
def solution(a,b):
    c=''
    d=len(a)
    for i in range(0,d):
        c=c+str(int(a[-(i+1)])+int(b[-(i+1)]))
    return c
print (solution('99','99'))