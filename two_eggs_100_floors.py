'''
two_eggs_100_floors.py
'''
def max_try(floors):
    for x in range(2,21):
        flrs=[]
        trys=[]
        s=0
        f=1
        n=int(floors/x)
        for i in range(0,x):
            f += n
            s += 1
            flrs.append(f if f<101 else 100)
            tr=flrs[i]-(1 if (i==0) else flrs[i-1] )+s
            trys.append(tr)
            #print(floors,x,n,i,f,s,tr)
        if flrs[-1]<100:
            flrs.append(floors)
            trys.append(floors-f+s)
        print(x,flrs,trys,max(trys))
           
print(max_try(100))