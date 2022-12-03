f = open("input.txt")
input = f.readlines()
input = list(map(lambda x : x.strip(),input))

res = 0
for line in input:
    half = len(line)//2
    compartment1 = line[:half]
    compartment2 = line[half:]
    duplicated = set(compartment1).intersection(compartment2).pop()
    res+=ord(duplicated) - 38 if duplicated.isupper() else ord(duplicated) - 96
print(res)

# Part 2
groups = []
curr_group = []
res2 = 0
for line in input:
    if len(curr_group) < 3:
        curr_group.append(line)
    else:
        groups.append(curr_group.copy())
        curr_group = [line]
groups.append(curr_group.copy())

for group in groups:
    elf1,elf2,elf3 = group
    duplicated = set(elf1).intersection(elf2).intersection(elf3).pop()
    res2 += ord(duplicated) - 38 if duplicated.isupper() else ord(duplicated) - 96
print(res2)