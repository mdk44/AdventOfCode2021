input_file = 'Day_07\\Input.csv'
# input_file = 'Day_07\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split(',')
for x in range(0, len(lines)):
    lines[x] = int(lines[x])

def find_sum(lines, i):
    result = 0
    for line in lines:
        result += abs(line - i)
    return result

def find_incr_sum(lines, i):
    result = 0
    for line in lines:
        for x in range(1, abs(line - i) + 1):
            result += x
    return result

# Part 1
sums = []
for x in range(0, max(lines) +1):
    sums.append(find_sum(lines, x))
print("Part 1: " + str(min(sums)))

# Part 2
sums = []
for x in range(0, max(lines) +1):
    sums.append(find_incr_sum(lines, x))
print("Part 2: " + str(min(sums)))