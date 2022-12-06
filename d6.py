line = open("input.txt").readline()
index1 = 0
index2 = 0
start_packer_marker = 4
start_message_marker = 14

res = 0
while index1 < len(line) -3 and index2 < len(line) -13:
    chars1 = set([line[index1],line[index1+1],line[index1+2],line[index1+3]])
    chars2 = set()
    [chars2.add(line[index2+i]) for i in range(14)]
    if len(chars1) == start_packer_marker and not res :
        res = index1+ start_packer_marker
    if len(chars2) == start_message_marker:
        res2 = index2 + start_message_marker
        break
    index1+=1
    index2+=1
print(res,res2)