from functools import cmp_to_key
input = list(map(eval,filter(lambda r : len(r)>0 ,map(lambda l : l.strip() ,open("input.txt").readlines()))))
divider1,divider2 = [[2]] , [[6]]
input.extend([divider1,divider2])
res =0
package_index = 0

def compare(p1,p2): # 1 = ordered ; -1 = not ordered ; 0 = undetermined
    if isinstance(p1,int) and isinstance(p2,int):
        return -1 if p1 > p2 else 1 if p1 < p2 else 0
    elif isinstance(p1,int):
        p1 = [p1]
    elif isinstance(p2,int):
        p2 = [p2]
    can_continue, is_ordered = True,False
    for i in range(len(p1)):
        if i == len(p2):
            return -1
        e1 = p1[i]
        e2 = p2[i]
        res_ord = compare(e1,e2)
        if res_ord == 1:
            return 1
        elif res_ord == -1:
            return -1
    return 0 if len(p1) == len(p2) else 1

for index in range(0,len(input),2):
    pack1 = input[index]
    pack2 = input[index+1]
    package_index+=1
    if compare(pack1,pack2) == 1 and pack1 != divider1:
        res += package_index

packs_sorted = sorted(input,reverse=True ,key=cmp_to_key(compare))
print(res, (packs_sorted.index(divider1)+1) *( packs_sorted.index(divider2)+1))