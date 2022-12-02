f = open("input.txt")
input = "".join(f.readlines()).split("\n\n")
formated = list(map(lambda x : list(map(lambda s : int(s),x.split("\n"))),input))
res = max( map( lambda l : sum(l), formated) )
print(res)

# Part 2
res2 = 0
totalEachCarries = list(map( lambda l : sum(l), formated) )
for i in range(3):
    curr_max = max(totalEachCarries )
    res2 +=  curr_max
    totalEachCarries.remove(curr_max)

print(res2)