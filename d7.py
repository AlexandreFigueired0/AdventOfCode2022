f = open("input.txt")
input = list(map(lambda l : l.strip(),f.readlines()))
max_size = 100000
curr_path = []
sizes = {"":0}
in_list = False
res = 0

def move_out():
    global curr_path
    curr_path = curr_path[0:-1]

def move_into(dir):
    global curr_path
    curr_path.append(dir)

def sum_size(size):
    global curr_path,sizes
    path = ""
    for i in range(len(curr_path)):
        path = "/".join(curr_path[:i+1])
        sizes[path] += size

def move_start():
    global curr_path
    curr_path = [""]

for cmd in input:
    if in_list and cmd[0] == "$":
        in_list = False

    if in_list:
        size,file = cmd.split()
        if size != "dir":
            sum_size(int(size))
        else :
            path ="/".join(curr_path + [file])
            sizes[path] = 0
    else:
        tokens = cmd.replace("$","").strip().split()
        tok1 = tokens[0]
        if tok1 == "cd":
            tok2 = tokens[1]
            if tok2 == "..":
                move_out()
            elif tok2 == "/":
                move_start()
            else :
                move_into(tok2)
        elif tok1 == "ls":
            in_list = True

for dir,size in sizes.items():
    if size <= max_size:
        res+= size

#Part2
total_space = 70000000
space_needed = 30000000
available_space = total_space - sizes[""]
print("available",available_space)
res2 = min(filter(lambda tup : tup[1] + available_space>= space_needed, sizes.items() ),key= lambda tup :tup[1])
print(res,res2)