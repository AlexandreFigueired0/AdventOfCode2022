f = open("input.txt")
input = f.readlines()
input = list(map(lambda x : x.strip(),input))

res = 0
for line in input:
    seen1 = set()
    seen2 = set()
    half = len(line)//2
    compartment1 = line[:half]
    compartment2 = line[half:]
    for i in range(half):
        item1 = compartment1[i]
        item2 = compartment2[i]
        seen1.add(item1)
        seen2.add(item2)
    duplicated = seen1.intersection(seen2).pop()
    res+=ord(duplicated) - 38 if duplicated.isupper() else ord(duplicated) - 96
print(res)