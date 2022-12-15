input = list(map(lambda l : l.strip() ,open("input.txt").readlines()))
input  = [line.split(" at ")[1:] for line in input]
sensors = set()
beacons = set()
row = 2000000
manhattan = lambda x1,y1,x2,y2 : abs(x1-x2) + abs(y1-y2)
cant_be_beacon_positions = set()
for i in range(len(input)):
    p1,p2 = input[i]
    p1 = p1[:p1.index(":")]
    x1 = int(p1[p1.index("=")+1:p1.index(",")])
    y1 = int(p1[p1.index("y")+2:])
    x2 = int(p2[p1.index("=")+1:p2.index(",")])
    y2 = int(p2[p2.index("y")+2:])
    sensors.add(((x1,y1),manhattan(x1,y1,x2,y2)))
    beacons.add((x2,y2))

def can_be_beacon(x,y):
    for s_pos,d in sensors:
        sx,sy = s_pos
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return False
    return True

end = False
for sens in sensors:
    s_pos,distance = sens
    sx,sy = s_pos
    if sy - distance <= row <= sy + distance:
        sens_dist_to_row = abs(sy-row)
        level = distance - sens_dist_to_row
        n_pos = 1 + 2*level
        xx = sx - level
        for i in range(n_pos):
            if (xx,row) not in beacons:
                cant_be_beacon_positions.add(xx)
            xx +=1
    #Part2, verificar as casas fora do range do sensor
    for dx in range(distance+2): 
        if end: break
        dy = (distance+1)-dx # dx + dy == distance
        for ddx,ddy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            outer_x = sx+(dx*ddx)
            outer_y = sy+(dy*ddy)
            if 0<=outer_x<=4000000 and 0<=outer_y<=4000000 and can_be_beacon(outer_x,outer_y):
                print("p2:",outer_x*4000000 + outer_y)
                end = True
                break
print("p1",len(cant_be_beacon_positions)) 