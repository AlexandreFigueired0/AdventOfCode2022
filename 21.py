input = list(map(lambda l : l.strip().split() ,open("input.txt").readlines()))
monkeys = {}
for line in input:
    monkeys[line[0].replace(":","")] = tuple(line[1:]) if len(line[1:]) > 1 else float(line[1])
me = "humn"

def get_monkey_val(monkey):
    m_action = monkeys[monkey]
    if isinstance(m_action,tuple):
        m1,op,m2 = m_action
        m1_val = get_monkey_val(m1)
        m2_val = get_monkey_val(m2)
        if monkey == "root":
            return m1_val, m2_val
        return eval(str(m1_val) + op + str(m2_val) )
    else:
        return m_action
min_v = 0
max_v = 10**13
mid_v = (min_v+max_v)/2
p1 = get_monkey_val("root")
print(int(eval(str(p1[0]) + monkeys["root"][1] + str(p1[1]))))
while True:
    monkeys[me] =mid_v
    v1,v2 = get_monkey_val("root")
    if v1 == v2:
        print(int(monkeys[me]))
        break
    elif v1 > v2:
        min_v = mid_v
        mid_v = (min_v+max_v)/2
    else: 
        max_v = mid_v
        mid_v = (min_v+max_v)/2

