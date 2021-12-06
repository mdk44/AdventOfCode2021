input_file = 'Day_06\\Input.csv'
# input_file = 'Day_06\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split(',')
for x in range(0, len(lines)):
    lines[x] = int(lines[x])

def grow_fish(lines, days):

    fish = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0
    }

    for line in lines:
        fish[str(line)] += 1
    x = 0
    while x < days:
        num_zero = fish["0"]
        for i in range(0, 8):
            fish[str(i)] = fish[str(i + 1)]
        fish["6"] += num_zero
        fish["8"] = num_zero
        x += 1
    return sum(fish.values())

print("Part 1: " + str(grow_fish(lines, 80)))
print("Part 2: " + str(grow_fish(lines, 256)))