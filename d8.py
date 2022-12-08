f = open("input.txt")
input = list(map(lambda l : l.strip(),f.readlines()))
grid = list(map(lambda l : list(map(lambda c : int(c),l) ),input))
R = len(grid)
C = len(grid[0])
DR = [1,0,-1,0]
DC = [0,1,0,-1]
res = 2*R + 2*(C-2)

def is_visible(row,col):
    curr_height = grid[row][col]
    viewed_from = 4 # n directions this tree is visible
    for i in range(4): #4 possible direction
        visible = True
        for scalar in range(1,max(R,C)):
            if not visible:
                continue
            new_row = row + DR[i] * scalar
            new_col = col + DC[i] * scalar
            if 0<=new_row<R and 0<=new_col<C: # valid pos
                other_height = grid[new_row][new_col]
                if other_height >= curr_height:
                    visible = False
                    viewed_from -=1
    return viewed_from >0

import math
res2 = 0
def seen_top(row,col):
    seen = 0
    dr = -1
    curr_height = grid[row][col]
    for scalar in range(1,R):
        new_row = row + dr * scalar
        if 0<=new_row<R: #valid pos
            seen +=1
            other_height = grid[new_row][col]
            if other_height >= curr_height: break
    return seen

def seen_right(row,col):
    seen = 0
    dc = 1
    curr_height = grid[row][col]
    for scalar in range(1,C):
        new_col = col + dc * scalar
        if 0<=new_col<C: #valid pos
            seen +=1
            other_height = grid[row][new_col]
            if other_height >= curr_height: break
    return seen

def seen_bottom(row,col):
    seen = 0
    dr = 1
    curr_height = grid[row][col]
    for scalar in range(1,R):
        new_row = row + dr * scalar
        if 0<=new_row<R: #valid pos
            seen +=1
            other_height = grid[new_row][col]
            if other_height >= curr_height: break
    return seen

def seen_left(row,col):
    seen = 0
    dc = -1
    curr_height = grid[row][col]
    for scalar in range(1,C):
        new_col = col + dc * scalar
        if 0<=new_col<C: #valid pos
            seen +=1
            other_height = grid[row][new_col]
            if other_height >= curr_height: break
    return seen

for row in range(1,R-1):
    for col in range(1,C-1):
        if is_visible(row,col): 
            res+=1
        seen_trees_direction = [seen_top(row,col),seen_right(row,col),seen_bottom(row,col),seen_left(row,col)] # ntrees visible from top,right,bottom,left
        scenic_score = math.prod(seen_trees_direction)
        res2 = max(scenic_score,res2)

print(res,res2)