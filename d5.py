from copy import deepcopy

f = open("input.txt")
input =[line[:-1:] for line in f.readlines()]
half_index = input.index("")
stacks_input = input[:half_index-1:]
stacks = [[] for i in range(int(input[half_index-1][-2]))]
moves = input[half_index+1::]
stack_nums = input[half_index-1]

for line in input:
    count = 0
    char_idx = 0
    while char_idx < len(line):
        curr_char = line[char_idx]
        if curr_char == '[' :
            stacks[count] = [line[char_idx+1]] + stacks[count]
        count+=1
        char_idx +=4

# Here input is formated
stacks2 = deepcopy(stacks)

for move in moves:
    nums =list(map(lambda i : int(i),filter(lambda x : x.isdigit(),move)))
    qtty,dest,src =nums[0], nums[-1],nums[-2]
    if len(nums) == 4 : qtty = qtty*10 + nums[1]
    dest_stack,src_stack =  stacks[dest-1],stacks[src-1]
    dest_stack2,src_stack2 =  stacks2[dest-1],stacks2[src-1]
    to_move = []
    to_move2 = []
    for i in range(qtty):
       to_move.append(src_stack.pop())
       to_move2.append(src_stack2.pop())#Part2
    [dest_stack.append(crate) for crate in to_move]
    [dest_stack2.append(crate) for crate in reversed(to_move2)]#Part2
for stack in stacks2:
    print(stack[-1],end="")
print()

print(stacks2)

    


