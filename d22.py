input = list(map(lambda l : l if "\n" not in l else l[:-1] ,open("input.txt").readlines()))
instructions_line = input[-1]
input = input[:-2]
wall = "#"
walls = set()
instructions = []
dirs_order = ["R","D","L","U"]
curr_dirs_idx  = 0
dirs = {"R" : (0,1), "D":(1,0), "L":(0,-1), "U":(-1,0)}
curr_dir = "R"
nrows = len(input)
ncols = max([len(row) for row in input])

row_lims = [[ncols, -1] for _ in range(nrows)]
col_lims = [[nrows, -1] for _ in range(ncols)]

for row, line in enumerate(input):
    for col in range(len(line)):
        c = line[col]
        if c ==wall:
            walls.add((row, col))

        if c in [".", "#"]: # inclusive lims
            row_lims[row][0] = min(row_lims[row][0], col)
            row_lims[row][1] = max(row_lims[row][1], col)
            col_lims[col][0] = min(col_lims[col][0], row)
            col_lims[col][1] = max(col_lims[col][1], row)
            max
r,c = 0,row_lims[0][0]
acc = 0
for char in instructions_line:
    if char.isdigit():
        acc = (acc*10) + int(char)
    else:
        if acc>0:
            instructions.append(acc)
            acc = 0
            instructions.append(char)
if acc > 0:
    instructions.append(acc)

def move(n):
    global r,c
    dr,dc = dirs[curr_dir]
    for _ in range(n):
        new_r,new_c = r + dr, c + dc
        if dr == 0:
            r_lims = row_lims[r]
            if new_c < r_lims[0] : # go to end of row
                new_c = r_lims[1]
            elif new_c > r_lims[1]: # go to start of row
                new_c = r_lims[0]
        else: # dc == 0
            c_lims = col_lims[c] 
            if new_r < c_lims[0]:
                new_r = c_lims[1]
            elif new_r > c_lims[1]:
                new_r = c_lims[0]
        if (new_r,new_c) in walls: return
        r,c = new_r,new_c

BASE = [(100, 50), (100, 99), (149, 50), (149, 99)]
UP = [(0, 50), (0, 99), (49, 50), (49, 99)] 
RIGHT =[(0, 100), (0, 149), (49, 100), (49, 149)]
LEFT = [(100, 0), (100, 49), (149, 0), (149, 49)]
DOWN = [(150, 0), (150, 49), (199, 0), (199, 49)]
FRONT = [(50, 50), (50, 99), (99, 50), (99, 99)]
# NEIGHBOURS = {"B" : [FRONT,LEFT,RIGHT,DOWN], "U":[FRONT,LEFT,RIGHT,DOWN], "R"}
def move3D(n):
    global r,c
    dr,dc = dirs[curr_dir]
    for _ in range(n):
        new_r,new_c = r+dr, c+dc
        if dr == 0:
            r_lims = row_lims[r]
            if new_c < r_lims:
                if 0 <= r <= 49: # UP
                    #go para o inicio da linha inversa LEFT
                    pass
                elif 50 <= r <= 99:
                    #go para meio da primeira linha to LEFT
                    pass
                elif 100 <= r <= 149:
                    #go inicio linha inversa UP
                    pass
                elif 150 <= r <= 199:
                    #
                    pass

        else:
            pass


for i in instructions:
    if isinstance(i,int):
        move(i)
    else:
        dr = 1 if i == "R" else -1
        curr_dirs_idx = (curr_dirs_idx+dr) % len(dirs_order)
        curr_dir = dirs_order[curr_dirs_idx]

print((r+1) * 1000 + (c+1)*4 + curr_dirs_idx)