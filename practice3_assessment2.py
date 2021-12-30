'''
palindrome
solution(s)
take all prefixes and chose the longest palindrome between them
if this chosen prefix contains at least 2 characters,cut this prefix from s and go back to the first step
1.,
s="aaacodedoc"=""
cut "aaa" => codedoc
cut "codedoc" => ""
2.,
s=codesignal => codesignal
'''
def palindrome(x):
    p=0
    xl=int(len(x)/2)
    print(x,xl,len(x)/2 )
    for i in range(xl):
        print (p,x[i],x[len(x)-i-1])
        if x[i]==x[len(x)-i-1] :
            p = p+1
        else:
            break
    print(p,xl)
    if p ==xl:
        return True
    else:
        return False

def prefix(s):
    res=s
    pl=0
    for i in range(len(res)):
        if  palindrome(res[0:i]) == True :
            print("palindrome",pl,res[0:i])
            pl = pl+1 
            continue
        else:
            res=res[pl:len(res)-pl]
    return res

def solution(s):
    res=s
    pl=0
    for i in range(len(res)):
        if  palindrome(res[0:i]) == True :
            print("palindrome",pl,res[0:i])
            pl = pl+1 
            continue
        else:
            res=res[pl:len(res)-pl]
    return res[pl:len(res)-pl]
print(solution("aaacodedoc"))