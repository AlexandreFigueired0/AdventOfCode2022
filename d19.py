input = list(map(lambda l : l.strip() ,open("input.txt").readlines()))
blueprints = [[] for j in range(len(input))]
bprint_id = -1
for line in input:
    bprint_id +=1
    words = line.split()
    index = -1
    for word in words:
        if word.isdigit() and index>=0:
            blueprints[bprint_id].append(int(word))
        index +=1
    blueprints[bprint_id][2] = (blueprints[bprint_id][2],blueprints[bprint_id][3])
    blueprints[bprint_id] = blueprints[bprint_id][:3] + blueprints[bprint_id][4:]
    blueprints[bprint_id][-2] = (blueprints[bprint_id][-2],blueprints[bprint_id][-1])
    blueprints[bprint_id] = blueprints[bprint_id][:-1]


def get_best(bp,time): #bfs
    best = 0
    ore_cost,clay_cost,obz_cost,geo_cost = bp
    initial = (0,0,0,0,1,0,0,0,time)
    queue = [initial]
    seen = set()
    while queue:
        state = queue.pop(0)
        ore,clay,obz,geo,ore_robots,clay_robots,obz_robots,geo_robots,t = state
        best = max(best,geo)
        if t== 0: continue
        max_ore = max([ore_cost, clay_cost, obz_cost[0], geo_cost[0]])
        if ore_robots>max_ore:
            ore_robots = max_ore
        if clay_robots>obz_cost[1]:
            clay_robots = obz_cost[1]
        if obz_robots>geo_cost[1]:
            obz_robots = geo_cost[1]
        if ore > max_ore+ore_robots:
            ore = max_ore+ore_robots
        if clay> obz_cost[1] +clay_robots:
            clay =obz_cost[1] + clay_robots
        if obz>geo_cost[1] + obz_robots:
            obz = geo_cost[1] + obz_robots
        state = ore,clay,obz,geo,ore_robots,clay_robots,obz_robots,geo_robots,t
        if state in seen : continue
        seen.add(state)
        new_ore = ore + ore_robots
        new_clay = clay + clay_robots
        new_obz = obz + obz_robots
        new_geo = geo + geo_robots
        if ore >= geo_cost[0] and obz >= geo_cost[1]: # build geo_robot
            queue.append((new_ore-geo_cost[0],new_clay,new_obz-geo_cost[1],new_geo,ore_robots,clay_robots,obz_robots,geo_robots+1,t-1))
        else: # test other builds only if we cant build geo
            queue.append((new_ore,new_clay,new_obz,new_geo,ore_robots,clay_robots,obz_robots,geo_robots,t-1))#dont build any robots
            if ore >=ore_cost and ore_robots < max_ore: #build ore_robot
                queue.append((new_ore - ore_cost,new_clay,new_obz,new_geo,ore_robots+1,clay_robots,obz_robots,geo_robots,t-1))
            if ore >= clay_cost and clay_robots < obz_cost[1]: #build clay robot
                queue.append((new_ore-clay_cost,new_clay,new_obz,new_geo,ore_robots,clay_robots+1,obz_robots,geo_robots,t-1))
            if ore >= obz_cost[0] and clay >= obz_cost[1] and obz_robots < geo_cost[1]:# build obz robot
                queue.append((new_ore-obz_cost[0],new_clay-obz_cost[1],new_obz,new_geo,ore_robots,clay_robots,obz_robots+1,geo_robots,t-1))
    return max(best,new_geo)

res = 0
res2 = 1
bprint_id = 0
for bp in blueprints:
    bprint_id +=1
    quality = get_best(bp,32)
    res2 *= quality
    res += quality * bprint_id
print(res,res2)