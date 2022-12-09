f = open("input.txt")
input = list(map(lambda l : [l.split()[0],int(l.split()[1])] ,f.readlines()))
hr,hc = 0,0
tails = [[0,0] for i in range(9)]
visited1 = set()
visited2 = set()
DIR = {'R':(0,1), 'U':(1,0), 'L':(0,-1), 'D':(-1,0)}
move = lambda r,c,dr,dc :(r+dr,c+dc)
touching = lambda r1,c1,r2,c2 : abs(r1-r2) <= 1 and abs(c1-c2) <= 1

for d,num in input:
    dr,dc = DIR[d]
    for _ in range(num):
        hr,hc = move(hr,hc,dc,dr)
        for i in range(len(tails)):
            if i == 0:
                tmp_hr = hr
                tmp_hc = hc
            else:
                tmp_hr = tails[i-1][0]
                tmp_hc = tails[i-1][1]
            if not touching(tmp_hr,tmp_hc,tails[i][0],tails[i][1]):
                if tmp_hr == tails[i][0]: #same row
                    tails[i][1]+= 1 if tmp_hc > tails[i][1] else -1
                elif tmp_hc == tails[i][1]: # same col
                    tails[i][0] += 1 if tmp_hr > tails[i][0] else -1
                else:
                    tails[i][0] += 1 if tmp_hr>tails[i][0] else -1
                    tails[i][1] += 1 if tmp_hc>tails[i][1] else -1
            if i == 0:
                visited1.add((tails[i][0],tails[i][1]))
            elif i == len(tails)-1:
                visited2.add((tails[i][0],tails[i][1]))

print(len(visited1),len(visited2))