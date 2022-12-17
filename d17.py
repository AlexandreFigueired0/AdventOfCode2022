input = open("input.txt").readline()
width = 7
starting_c = 2
n_rocks_stopped = 0
blocked = set()

def horizontal(x_lo,y_lo):
    res = []
    for dx in range(0,4):
        res.append((x_lo+dx,y_lo))
    return res

def plus(x_lo,y_lo):
    res = []
    for dx in range(0,3):
        res.append((x_lo+dx,y_lo+1))
    return res + [(x_lo+1,y_lo), (x_lo+1,y_lo+2)]

def L(x_lo,y_lo):
    res = []
    for dx in range(0,3):
        res.append((x_lo+dx,y_lo))
    return res + [(x_lo + 2,y_lo+1), (x_lo+2,y_lo+2)]

def vertical(x_lo,y_lo):
    res = []
    for dy in range(0,4):
        res.append((x_lo,y_lo+dy))
    return res

def square(x_lo,y_lo):
    return [ (x_lo,y_lo), (x_lo,y_lo+1), (x_lo+1,y_lo+1), (x_lo+1,y_lo) ]

def move(rock,dir):
    res = []
    dx,dy = dir
    for rx,ry in rock:
        new_rx = rx+dx
        new_ry = ry+dy
        if  new_ry < 0 or new_rx >= width or new_rx <0 or (new_rx,new_ry) in blocked:
            return rock
        res.append((new_rx,new_ry))
    return res


shapes = {0:horizontal, 1:plus , 2:L, 3:vertical, 4:square}
shape_index = 0
input_index = 0
top = -1
L = 1000000000000 # 2022 for p1
add = 0

def top_view():
    tops = [0 for _ in range(7)] # 7 possitons
    for (x,y) in blocked:
        tops[x] = max(tops[x],y)
    m = max(tops)
    return tuple([t-m for t in tops])

seen = {}
add = 0
while n_rocks_stopped < L:
    f = shapes[shape_index]
    shape_index = (shape_index+1) % len(shapes)
    x_lo = 2
    y_lo = top + 4
    rock = f(x_lo,y_lo)
    while True: #move horizontally then down
        c = input[input_index]
        input_index =(input_index + 1) % len(input)
        dx = 1 if c == ">" else -1
        new_rock = move(rock,(dx,0)) # if it was blocked do nothing
        fall_rock = move(new_rock,(0,-1))
        if fall_rock == new_rock: #blocked falling, stop
            top = max(top,max(fall_rock,key=lambda tup : tup[1])[1])
            n_rocks_stopped +=1
            blocked.update(fall_rock)
            top_v = top_view()
            if (top_v,shape_index,input_index) in seen:
                old_nr,old_top =  seen[(top_v,shape_index,input_index)]
                dt = top-old_top
                d_nr = n_rocks_stopped-old_nr
                n_cycles = (L-n_rocks_stopped)//d_nr
                add += n_cycles*dt
                n_rocks_stopped += n_cycles*d_nr
            seen[(top_v,shape_index,input_index)] = (n_rocks_stopped,top)
            break
        rock = fall_rock

print(top+1+add)