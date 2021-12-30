'''minesweeper
on each turn the player clicks on a cell
-if it has a bomb- game over,player loses
-if not, a number appears representing how many mines are in the neighbouring 8 cells
-if the revealed number is zero then each of the neighbouring cells are automatically revealed in the same way
array field representing the distribution of the bombs in a rectangular field
x,y representing the coordinates of the player''s first clicked cell, x=row, y =column, both 0 based
your task is to return an integer matrix of the same dimension as field after applying this click 
if a cell remains concealed the corresponding element should have a value of -1
it is guaranteed  that the clicked cell doesn''t contain a mine
1.,
field = 
[[false,true,true],
 [true,false,true],
 [false,false,true]] and x=1 y=1 has 5 neighbors with a bomb, and the other elements should be -1 since no other cell would be expanded
2.,
field = 
 [[true,false,true,true,false],
 [true,false,false,false,false],
 [false,false,false,false,false],
 [true,false,false,false,false]] and x=3 y=2
solution(field, x,y) =
[[-1,-1,-1,-1,-1],
 [-1, 3, 2, 2, 1],
 [-1, 2, 0, 0, 0],
 [-1, 1, 0, 0, 0]]
[[-1, -1, -1, -1, -1],
 [-1, 3, 2, 2, 1],
 [-1, 2, 0, 0, 0],
 [-1, 1, 0, 0, 0]]

'''
def initdisplay(field):
    res=[]
    for i in range(len(field)):
        row=[]
        for j in range(len(field[0])):
            row.append(-1)
        res.append(row)
    return res
def countbombs(field,x,y):
    bombs=0
    for i in (x-1,x,x+1):
        for j in (y-1,y,y+1):
            if i>=0 and i<len(field) and j>=0 and j<len(field[0]) and (i!=x or j!=y):
                if field[i][j]==True:
                    bombs = bombs + 1
    return bombs
def revealneighbours(field,res,x,y):
    zeroes=0
    for i in (x-1,x,x+1):
        for j in (y-1,y,y+1):
            if i>=0 and i<len(field) and j>=0 and j<len(field[0]) and (i!=x or j!=y):
                if res[i][j] == -1 :
                    bombs=countbombs(field,i,j)
                    res[i][j]=bombs
                    if bombs == 0 :
                        zeroes = zeroes + 1
                    #print (x,y,i,j,bombs,zeroes)
    return zeroes

def checkforzeroes(field,res):
    zeroes=0
    for i in range(len(res)):
        for j in range(len(res[0])):
            if res[i][j] == 0 :
                zeroes=revealneighbours(field,res,i,j)
    return zeroes

def solution(field, x,y):
    res=initdisplay(field)
    res[x][y]=countbombs(field,x,y)
    #print (x,y,res[x][y])
    if res[x][y] == 0 :
        zeroes=revealneighbours(field,res,x,y)
    while zeroes > 0 :
        zeroes=checkforzeroes(field,res)
    #print(res)
    return(res)
res=[]
#field = [[False,True,True],[True,False,True],[False,False,True]]
#print(solution(field,1,1))
field = [[True,False,True,True,False],
 [True,False,False,False,False],
 [False,False,False,False,False],
 [True,False,False,False,False]]
print(solution(field,3,2))


