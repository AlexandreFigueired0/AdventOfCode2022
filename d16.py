import functools
input = list(map(lambda l : l.strip().split(";") ,open("input.txt").readlines()))
valves_network = {}
valves = {}
for line in input:
    p1,p2 = line
    neighbours_bad = list(filter(lambda c : c.isupper(),p2))
    neighbours = []
    for i in range(0,len(neighbours_bad)-1,2):
        neighbours.append(neighbours_bad[i] + neighbours_bad[i+1])
    curr_valve = p1[6:8]
    valves[curr_valve] = int(p1[p1.index("=")+1:])
    valves_network[curr_valve] = neighbours
start = "AA"
time = 30

@functools.lru_cache(maxsize=None)
def explore(curr_valve,time,opened):
    if time <= 0:
        return 0
    res = 0
    if curr_valve not in opened:
        flow_rate = (time-1) * valves[curr_valve]
        new_opened =opened + (curr_valve,)
        for v in valves_network[curr_valve]:
            if flow_rate != 0: # in case we open the valve
                res = max(res, flow_rate  + explore( v, time-2 , new_opened ))
            res = max(res, explore(v , time-1,opened))
    return res

@functools.lru_cache(maxsize=None)
def explore2(curr_valve,time,opened):
    if time <= 0:
        return explore(start,26,opened)
    res = 0
    if curr_valve not in opened:
        flow_rate = (time-1) * valves[curr_valve]
        if flow_rate != 0: # in case we open the valve
            new_opened =opened + (curr_valve,)
            for v in valves_network[curr_valve]:
                    res = max(res, flow_rate  + explore2( v, time-2 , new_opened ))
    for v in valves_network[curr_valve]:
        res = max(res, explore2(v , time-1,opened))
    return res


print(explore(start,30,()))
print(explore2(start,26,()))



