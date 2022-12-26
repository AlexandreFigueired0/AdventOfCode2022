input = list(map(lambda l : l.strip() ,open("input.txt").readlines()))
res = 0

to_snafu = {"=":-2, "-":-1,"0":0, "1":1,"2":2}
to_int = {d: s for s, d in to_snafu.items()}

for line in input:
    curr_p = 0
    num =0
    for ch in line[::-1]:
        num += to_snafu[ch] * 5**curr_p
        curr_p+=1
    res += num

def to_snafu(num):
    res = ''

    while num > 0:
        num, place = (num+2)//5, (num+2)%5
        res += to_int[place-2]

    return res[::-1]
print(to_snafu(res))