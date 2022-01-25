'''
u r given an array of rectangles where 
rectangles[i] =[li,wi] represents a rectangle of length li and width wi
you can cut the ith rectangle to form a square with a side length of k
if k<=li and k<=wi
[4,6] => k=4
let maxlen be the side length of the largest square you can obtain 
from any given rectangles
return the number of rectangles that can make a square with the side length
of maxlen
[[5,8],[3,9],[5,12],[16,5]] => 3
[5,3,5,5]
'''
rectangles = [[5,8],[3,9],[5,12],[16,5]]
maxlen=0
numrsq=0
for r in rectangles:
    sq=min([r[0],r[1]])
    if sq > maxlen:
        maxlen=sq 
        numrsq=1
    elif sq == maxlen:
        numrsq += 1
print(rectangles,maxlen,numrsq)
