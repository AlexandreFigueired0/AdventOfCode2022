from math import lcm
input = list(map(lambda l : l.strip() ,open("input.txt").readlines()))
start_pos = None
end_pos = None
height = len(input) -2
width = len(input[0]) -2
blizzards = dict()
walls = set()
memo = {}
DIRS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
period = lcm(width , height)
for i in range(len(input)):
    for j in range(len(input[0])):
        ch = input[i][j]
        if ch == "#" : walls.add((i,j))
        elif ch == "." and start_pos == None : start_pos = (i,j)
        elif ch != "." : # blizard
            if ch not in blizzards:
                blizzards[ch] = set([(i,j)])
            else:
                blizzards[ch].add((i,j))
        if i == len(input)-1 and ch == ".":
            end_pos = (i,j)

def move_blizzards(b):
    res = {}
    for dir,positions in b.items():
        if dir not in res:
            res[dir] = set()
        for r,c in positions:
            dr,dc = DIRS[dir]
            rr,cc = ((r+dr)-1)%(height) + 1,((c+dc)-1)%(width) + 1
            res[dir].add((rr,cc))
    all = set([pos for vals in res.values() for pos in vals ])
    return res,all

blizzards_states = [None] * period
all = set([pos for vals in blizzards.values() for pos in vals ])
blizzards_states[0] = all
b = {}
b[0] = blizzards
for t in range(1, period):
    blzs =  move_blizzards(b[t-1])
    blizzards_states[t] =blzs[1]
    b[t] = blzs[0]
    
def print_grid():
    grid = [[0 for j in range(len(input[0]))] for _ in range(len(input))]
    for i in range(len(input)):
        for j in range(len(input[0])):
            pos=i,j
            if pos in walls:
                grid[i][j] = "#"
            else:
                drawn = False
                for b in "<>v^":
                    if pos in blizzards[b]:
                        drawn = True
                        if grid[i][j] == 0:
                            grid[i][j] = b
                        elif str(grid[i][j]) in "<>v^":
                            grid[i][j] = 2
                        elif grid[i][j] >= 2:
                            grid[i][j]+=1
                if not drawn:
                    grid[i][j] = "."
            print(grid[i][j],end="")
        print()

p1 = False
queue = [(start_pos,0,False,False)] # state is curr_pos and minutes
seen = set()
while queue:
    curr = queue.pop(0)
    (r,c), minutes,e,s = curr
    if curr in seen : continue
    seen.add(curr)
    if (r,c) == end_pos and not p1: #first time going
        p1 = True
        print("p1",minutes)
        e = True
    if (r,c) == start_pos and e: # go back to start
        s = True
    if (r,c) == end_pos and s and e: # reached end again
        print("p2",minutes)
        break   
    new_blizzards =  blizzards_states[(minutes+1) % period]
    for dir in [(-1,0),(0,1),(1,0),(0,-1),(0,0)]:
        dr,dc = dir
        rr,cc = r+dr, c+dc
        if (rr,cc) not in walls and (rr,cc) not in new_blizzards and 0<=rr<=height+2 and  0<= cc <= width+2:
            queue.append(((rr,cc),minutes+1,e,s))

#245
# 798