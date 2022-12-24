input = list(map(lambda l : l.strip() ,open("input.txt").readlines()))
elves = set()
for r in range(len(input)):
    for c in range(len(input[0])):
        ch = input[r][c]
        if ch == "#": #Elf
            elves.add((r,c))
directions = ["n","s","w","e"]
DIRS = {"n":(-1,0), "s":(1,0), "e":(0,1), "w":(0,-1)}
round = 0

def has_adjacent(r,c):
    for dr,dc in [(1,0), (-1,0), (1,1), (1,-1), (-1,1),(-1,-1), (0,1), (0,-1)]:
        if (r+dr,c+dc) in elves:
            return True
    return False

def round_left(l):
    return l[1:] + [l[0]]

def empty_tiles():
    len_ = max(elves,key= lambda pos : pos[1])[1]-min(elves,key= lambda pos : pos[1])[1] +1
    height = max(elves,key= lambda pos : pos[0])[0] -min(elves,key= lambda pos : pos[0])[0]+1
    return len_ * height - len(elves)

while True:
    if round == 10:
        print(empty_tiles())
    round +=1
    considers = dict()
    for r,c in elves:
        if not has_adjacent(r,c) :
            considers[(r,c)] = (r,c)
        else: # test positons
            for dir in directions:
                adjacent = False
                dr,dc = DIRS[dir]
                new_r,new_c =0,0
                if dir == "n" or dir == "s": # change col
                    for ddc in [0,1,-1]:
                        new_r,new_c = r+dr, c+ddc
                        if (new_r,new_c) in elves:
                            adjacent = True
                            break
                else: #change row
                    for ddr in [0,1,-1]:
                        new_r,new_c = r+ddr, c+dc
                        if (new_r,new_c) in elves:
                            adjacent = True
                            break

                if not adjacent:
                    considers[(r,c)] = (r+dr,c+dc)
                    break

    vals = list(considers.values())
    n_elves = len(elves)
    count = 0
    for curr_pos, considered_pos in considers.items():
        if vals.count(considered_pos) > 1: # another elf wants to go here, so dont move
            count +=1
            continue 

        elves.remove(curr_pos)
        elves.add(considered_pos)

        if curr_pos == considered_pos:
            count+=1
    if count == n_elves:
        print(round)
        break
    directions = round_left(directions)