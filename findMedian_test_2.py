import math
#	Display the median price of a given beverage type. 
#	Given an n sized unsorted array of integer prices, write a function findMedian([]) to return the median price. 
#	You can assume that the array will contain at least one element.
#	findMedian([1,6,3,5,8,9,4,10,2]) => 5
#	findMedian([1,6,3,5,8,9,4,10,2,7]) => 5.5

#	I also assumed that the task wasn't to write a sort function O(nlogn) performance
test1=[1,6,3,5,8,9,4,10,2] 
test2=[1,6,3,5,8,9,4,10,2,7]
test3=[123]               # to test for the guaranteed minimum 1 item 

def findMedian(unsorted): #s.sort() could be used if we don't mind the in-place sorting
    s=sorted(unsorted) 
    ctr=int(len(s)/2)
    return  s[ctr] if len(s) % 2 > 0 else sum(s[ctr-1:ctr+1])/2.0

print(test1,sorted(test1),findMedian(test1))
print(test2,sorted(test2),findMedian(test2))
print(test3,sorted(test3),findMedian(test3))