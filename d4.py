f = open("input.txt")
input = f.readlines()
input = list(map(lambda x : x.strip(),input))
pairs = list(map (lambda x : x.split(","),input))
res = 0
for pair in pairs:
    elf1,elf2 = pair
    elf1 = list(map(lambda x : int(x),elf1.split("-")))
    elf2 = list(map(lambda x : int(x),elf2.split("-")))
    section1 = [int(elf1[0]),int(elf1[1])]
    section2 = [int(elf2[0]),int(elf2[1])]
    if(section1[0] <= section2[0] and section1[1]>= section2[1]) or \
        (section2[0]<= section1[0] and section2[1]>= section1[1]):
        res+=1
print(res)

# Part2
res2 = 0
for pair in pairs:
    elf1,elf2 = pair
    elf1 = list(map(lambda x : int(x),elf1.split("-")))
    elf2 = list(map(lambda x : int(x),elf2.split("-")))
    section1 = set([x for x in range(elf1[0],elf1[1]+1)])
    section2 = set([x for x in range(elf2[0],elf2[1]+1)])
    if len(section1.intersection(section2)) > 0 :
        res2 +=1
print(res2)