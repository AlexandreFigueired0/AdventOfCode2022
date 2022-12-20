input = list(enumerate(list(map(lambda l : int(l.strip()) * 811589153 ,open("input.txt").readlines()))))
not_done = input[:]

print()
for k in range(10): #remove cylce and multplication for p1
    for num in not_done:
        if num[1] == 0: continue
        steps = num[1] % (len(input)-1) 
        index = input.index(num)
        new_index = ((index+steps) % len(input)) + ((index+steps)//len(input))
        input.remove(num)
        input = input[:new_index] + [num] + input[new_index:]


zero_index = 0
for _,n in input:
    if n == 0:
        zero_index = input.index((_,0))
        break

res= sum([input[(1000+zero_index)%len(input)][1],input[(2000+zero_index)%len(input)][1],input[(3000+zero_index)%len(input)][1]])
print(res)