input = "".join(open("input.txt").readlines()).split("\n\n")
input = list(map(lambda l : list(map(lambda x : x.strip(),l.split("\n"))),input))
max_cylces = 10000 
gcm = 1
class Monkey():
    def __init__(self,l) :
        global gcm
        n,starting,op,test,true,false = l
        self.n = int(n.split()[-1][0:-1])
        self.items = []
        for word in starting.split(" "):
            if ',' in word :
                word = word.replace(",","")
            if str.isdigit(word):
                self.items.append(int(word))
        self.operation = op[op.index("=")+1:].strip()
        self.test = int(test.split()[-1])
        gcm *=self.test
        self.true = int(true[-1])
        self.false = int(false[-1])
        self.inspections = 0
        
monkeys = list(map(Monkey,input))
for _ in range(max_cylces):
    for monkey in monkeys:
        for worry in monkey.items:
            monkey.inspections +=1
            worry = eval(monkey.operation.replace("old",str(worry)))
            # worry = worry//3
            worry %= gcm
            if worry % monkey.test == 0:
                monkeys[monkey.true].items.append(worry)
            else:
                monkeys[monkey.false].items.append(worry)
        monkey.items = []

inpects = sorted(list(map(lambda m : m.inspections,monkeys)))
print(inpects[-1] * inpects[-2])