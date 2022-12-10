input = list(map(lambda l : l.split() ,open("input.txt").readlines()))
x=1
curr_cicle = 0
sum_cicles = [ 20, 60 ,100, 140, 180,220]
res = 0
check_sum_cicles = lambda : curr_cicle in sum_cicles
crt_width,crt_height = 40,6
crt = [["." for j in range(crt_width)] for i in range(crt_height)]
sprite_pos = ["." for j in range(crt_width)]
crt_row,crt_col = 0,0

def draw():
    global crt_col,crt_row
    crt[crt_row][crt_col] = "#"  if x-1<=crt_col<=x+1 else "."
    crt_col+=1
    if crt_col == crt_width:
        crt_col = 0
        crt_row+=1

for line in input:
    if line[0] == "noop":
        curr_cicle +=1
        draw()
        res = res + x*curr_cicle if check_sum_cicles() else res
    else:
        _,n = line
        curr_cicle +=1
        draw()
        res = res + x*curr_cicle if check_sum_cicles() else res
        curr_cicle +=1
        draw()
        res = res + x*curr_cicle if check_sum_cicles() else res
        x += int(n)
print(res)

[print("".join(line)) for line in crt]