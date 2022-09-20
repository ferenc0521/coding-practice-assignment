def fill_buckets(a):
    buckets=[0]*100
    for age in a:
        buckets[age] = buckets[age] +1
    return buckets

def count_buckets(b):
    stats=[[0,0]]*100
    for i in range(1,100):
        sumbefore=0
        for j in range(1,i):
            sumbefore += b[j]
        sumafter=0   
        for j in range(i,100):
            sumafter += b[j]
        stats[i]=[sumbefore,sumafter]
    return stats
            
def find_median(a):
    b=fill_buckets(a)
    print(b)
    stats=count_buckets(b)
    print(stats)
    median=0
    for bucket in range(1,len(stats)):
        if stats[bucket][0] > stats[bucket][1]:
            median=bucket-1
            break
    return median

print(find_median([1,25,3,50,75])) # 25

# two of them have the same count before and after
# if the median is on an element with 0 count