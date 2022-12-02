f = open("input.txt")
input = f.readlines()
opponent_rock = "A"
opponent_paper = "B"
opponent_scissors = "C"
my_rock = "X"
my_paper = "Y"
my_scissors = "Z"
points_play = {my_rock : 1 , my_paper :2 , my_scissors : 3}
points_round = {(opponent_rock,my_paper):6, (opponent_rock,my_scissors):0, (opponent_paper,my_rock):0,
                (opponent_paper,my_scissors):6, (opponent_scissors,my_rock):6 , (opponent_scissors,my_paper):0}
games = list(map(lambda s : s.strip(),input))
res = 0
for round in games:
    opponent_play = round[0]
    my_play = round[-1]
    res+= points_play[my_play] + points_round.get((opponent_play,my_play),3)
print(res)

# Part 2
lost = "X"
draw = "Y"
win = "Z"
points_round = {lost:0,draw:3,win:6}
piece_to_play= {(opponent_rock,win):my_paper , (opponent_rock,lost): my_scissors,  (opponent_paper,win): my_scissors,
                 (opponent_paper,lost): my_rock ,  (opponent_scissors,lost): my_paper ,  (opponent_scissors,win): my_rock,
                 (opponent_paper,draw): my_paper ,  (opponent_scissors,draw): my_scissors ,  (opponent_rock,draw): my_rock}
res2 = 0
for round in games:
    opponent_play = round[0]
    round_res = round[-1]
    my_play = piece_to_play[(opponent_play,round_res)]
    res2 += points_round[round_res] + points_play[my_play]
print(res2)