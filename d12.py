input = list(map(lambda l : list(map( lambda c : ord(c) if c!= "E" and c != "S" else c ,l.strip())) ,open("input.txt").readlines()))
start_height = ord("a")
end_height = ord("z")
R = len(input)
C = len(input[0])
DIR = [(0,1),(1,0),(0,-1),(-1,0)] # r, d, l ,u

def neighbours(r,c,s):
    res = []
    height = input[r][c]
    for dr,dc in DIR:
        new_row,new_col = r + dr , c + dc
        if 0<= new_row <R and 0<= new_col < C: #valid pos
            neighbour_height = input[new_row][new_col]
            if neighbour_height - height <= 1:
                res.append(((new_row,new_col),s+1))
    return res

lowest_points = []
for r in range(R):
    for c in range(C):
        if input[r][c] == start_height:
            lowest_points.append((r,c))

        elif "S" == input[r][c]:
            s_pos = (r,c)
            lowest_points.append((r,c))
        elif "E" == input[r][c]:
            e_pos = (r,c)
input[s_pos[0]][s_pos[1]] = start_height
input[e_pos[0]][e_pos[1]] = end_height

steps = []
for start_pos in lowest_points:
    visited = []
    queue = []
    visited.append(start_pos)
    queue.append((start_pos,0)) # pos and nsteps
    while queue:
        pos,s = queue.pop(0)
        r,c = pos
        for n in neighbours(r,c,s):
            if n[0] == e_pos:
                steps.append(n[1])
                if start_pos == s_pos:
                    print("part1",n[1])
                break
            if n[0] not in visited:
                visited.append(n[0])
                queue.append(n)
print("part2",min(steps))