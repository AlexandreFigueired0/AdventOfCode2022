import numpy as np
input = list(map(lambda l : list(map(int,l.strip().split(","))) ,open("input.txt").readlines()))
cubes = set(map(tuple,input))
res = 0

outside = set()
inside = set()
def reaches_outside(pos):
    x,y,z = pos
    if (x,y,z) in outside:
        return True
    if (x,y,z) in inside:
        return False
    seen = set()
    stack = [(x,y,z)]
    while stack:
        x,y,z = stack.pop(0)
        if (x,y,z) in cubes: continue
        if (x,y,z) in seen: continue
        seen.add((x,y,z))
        if len(seen) > 2000: # arbitrary value, if seen reaches this far it means we must be outside
            for p in seen:
                outside.add(p)
            return True
        for pos in range(3):
            front = [x,y,z]
            back = [x,y,z]
            front[pos] +=1
            back[pos] -=1
            stack.append((front[0],front[1],front[2]))
            stack.append((back[0],back[1],back[2]))
    for p in seen:
        inside.add(p)
    return False

res2 = 0
for x,y,z in cubes:
    connections = 0
    cube = [x,y,z]

    for pos in range(3):
        front = [x,y,z]
        back = [x,y,z]
        front[pos] -=1
        back[pos] -=1
        
        connections += tuple(front) in cubes
        connections += tuple(back) in cubes

        if reaches_outside(front) : res2 +=1
        if reaches_outside(back) : res2 +=1

    res += 6 - connections
print(res,res2)