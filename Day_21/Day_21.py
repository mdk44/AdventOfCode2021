# p1_space = 4 # test
# p2_space = 8 # test
p1_space = 3 # actual
p2_space = 7 # actual
p1_score = 0
p2_score = 0
turn = 0
dice = 0

def roll_fixed_die(player):
    if player == 1:
        s = p1_space
    elif player == 2:
        s = p2_space
    d = int(str(dice)[-1])
    for i in range(0, 3):
        d += 1
        s += d
        if s > 10:
            s = s % 10
    return s, d

winner = False
while winner == False:
    space, die = roll_fixed_die(1)
    p1_space = space
    dice += 3
    p1_score += space
    if p1_score > 999:
        winner = True
    else:
        space, die = roll_fixed_die(2)
        p2_space = space
        dice += 3
        p2_score += space
        if p2_score > 999:
            winner = True

print("Part 1: " + str(min(p1_score, p2_score) * dice))
print(p1_score, p2_score, dice, p1_space, p2_space)
