'''
You are given an array of integers as input 
(you can assume the array is well formed and won’t contain an element that is not an integer). 
Write a method that takes this array and finds the subarray 
whose sum of elements is greater than the sum of elements for any other possible subarray.
For example, let’s say our input is this array: [1, 3, -2, -4, 5, 6, 1, -3, -2, 1, 0]. 
A subarray must consist of contiguous elements. 
This means [1, 3, -2] is a valid subarray but [1, -2, 5] is not because it skips over the 3 and -4. 
For this sample input, your method would return [5, 6, 1] because the sum of the elements for this subarray, 12, 
is larger than the sum of elements for any other subarray.
Hint: Once you have a solution, try running it with some other sample arrays and 
think of some corner cases you would test.
'''
def max_sum_subarray(a):
    n=len(a)
    if n<1:
        return []
    max_sum=a[0]
    result=[a[0]]
    for i in range(n):
        for j in range(i+1,n+1):
            subarray=a[i:j]
            subarray_sum=sum(subarray)
            if subarray_sum > max_sum:
                max_sum=subarray_sum
                result=subarray
            #print(max_sum,result,i,j,subarray,subarray_sum)
    return result
tests=[
    [1, 3, -2, -4, 5, 6, 1, -3, -2, 1, 0], #original
    [1], #single element
    [-1, -3, -2, -4, -5, -6, -1, -3, -2, -1], #all negative
    [-3, -6, 0, -1], #all negative but one
    [0, -1, -3, -2, -4, -5, -6, 0, 0, -1, -3, -2, -1], #all negative but two
    []  #empty
]  
for test in tests:    
    result= max_sum_subarray(test)         
    print(test,result,sum(result) if len(result)>0 else -999999999)