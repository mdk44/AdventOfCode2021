import re

# input_file = 'Day_04\\Input.csv'
input_file = 'Day_04\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

numcards = 0
for line in lines:
    if line == '':
        numcards += 1

nums = map(int, lines[0].split(','))

def create_bingocards(lines):
    cards = []
    x = 0
    cards.append([])
    for line in range(2, len(lines)):
        if lines[line] != '':
            numbers = re.findall(r"\d+",lines[line])
            cards[x].append(map(int, numbers))
        else:
            x += 1
            cards.append([])
    return cards

def print_bingocards(cards):
    for card in cards:
        for y in card:
            print(y)
        print('')

def check_rows(cards):
    for card in cards:
        for y in card:
            if sum(y) == -5:
                return cards.index(card)
    return -1

def check_columns(cards):
    for card in cards:
        for x in range(0, 5):
            result = 0
            for y in range(0, 5):
                result += card[y][x]
            if result == -5:
                return cards.index(card)
    return -1

def mark_cards(cards, num):
    for card in cards:
        for y in range(0, 5):
            for x in range(0, 5):
                if card[y][x] == num:
                    card[y][x] = -1
    return num

def sum_card(card):
    cum_sum = 0
    for y in range(0, 5):
        for x in range(0, 5):
            if card[y][x] != -1:
                cum_sum += card[y][x]
    return cum_sum

# Part 1
bingocards = create_bingocards(lines)
winning_num = -1
winning_card = -1
for num in nums:
    mark_cards(bingocards, num)
    result = (check_rows(bingocards), check_columns(bingocards))
    for res in result:
        if res != -1:
            winning_num = num
            winning_card = res
            break
    if winning_num != -1:
        break

part_1_sum = sum_card(bingocards[winning_card]) * winning_num
print("Part 1: " + str(part_1_sum))

# Part 2
bingocards = create_bingocards(lines)
winners = []
for i in range(0, numcards):
    winners.append(1)

for num in nums:
    mark_cards(bingocards, num)
    for i in range(0, numcards):
        if winners[i] != 1:
            pass
        else:
            result = (check_rows(bingocards[i]), check_columns(bingocards[i]))
        for res in result:
            if res != -1:
                winners[i] = 0
                break
        if sum(winners) == 1:
            break

final_card = 0
for i in range(0, len(winners)):
    if winners[i] == 1:
        final_card = i

print_bingocards(bingocards[final_card])