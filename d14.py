input = list(map(lambda l : list(map(eval,l.strip().split(" -> "))),open("input.txt").readlines()))
blocked = set()
sand_src_pos = 500,0
abyss = 0
n_units_sand = 0

def get_rock_pos(x1,y1,x2,y2):
    res = []
    if x1 == x2: #vertical 
        for y in range(min(y1,y2),max(y1,y2)+1):
            res.append((x1,y))
    else :
        for x in range(min(x1,x2),max(x1,x2)+1):
            res.append((x,y1))
    return res

for line in input: # getting rocks pos
    for i in range(len(line)-1):
        x1,y1 = line[i]
        x2,y2 = line[i+1] 
        abyss = max(abyss,y1,y2)
        blocked.update(get_rock_pos(x1,y1,x2,y2))
floor = abyss +2

def sand_fall(sx,sy):
    res = sx,sy
    if sy +1 < floor:
        if (sx,sy+1) not in blocked :
            res = (sx,sy+1)
        elif (sx-1,sy+1) not in blocked:
            res = (sx-1,sy+1)
        elif (sx+1,sy+1) not in blocked:
            res = (sx+1,sy+1)
    return res
    
end,p1 = False, True
while not end:
    sx,sy = sand_src_pos
    n_units_sand +=1
    while True:
        new_sx,new_sy = sand_fall(sx,sy)
        if new_sy == 0: # sand source blocked
            print("p2",n_units_sand)
            end = True
            break
        if new_sy == sy : # Didnt fall bcz is blocked
            blocked.add((sx,sy))
            break
        if new_sy == abyss and p1: # Sand fell into the abyss
            print("p1",n_units_sand-1)
            p1 = False
        sx,sy = new_sx,new_sy