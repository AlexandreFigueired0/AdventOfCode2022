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
max_cols =len(input[0])
nrows = len(input)
ncols = max([len(row) for row in input])

row_lims = [[ncols, -1] for _ in range(nrows)]
col_lims = [[nrows, -1] for _ in range(ncols)]

for row, line in enumerate(input):
    for col in range(len(line)):
        c = line[col]
        if c ==wall:
            walls.add((row, col))

        if c in [".", "#"]:
            row_lims[row][0] = min(row_lims[row][0], col)
            row_lims[row][1] = max(row_lims[row][1], col)
            col_lims[col][0] = min(col_lims[col][0], row)
            col_lims[col][1] = max(col_lims[col][1], row)
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
        if (r,c) in walls: return
        new_r,new_c = r + dr, c + dc
        if dr == 0:
            len_ = row_lims[r][1] -  row_lims[r][0] +1
            new_c = (new_c - row_lims[r][0])% len_ + row_lims[r][0]
        else: # dc == 0
            len_ = col_lims[c][1] - col_lims[c][0] +1
            new_r = (new_r - col_lims[c][0]) % len_ + col_lims[c][0]
        if (new_r,new_c) in walls: return
        r,c = new_r,new_c


for i in instructions:
    if isinstance(i,int):
        move(i)
    else:
        dr = 1 if i == "R" else -1
        curr_dirs_idx = (curr_dirs_idx+dr) % len(dirs_order)
        curr_dir = dirs_order[curr_dirs_idx]

print((r+1) * 1000 + (c+1)*4 + curr_dirs_idx)