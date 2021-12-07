import re

# input_file = 'Day_05\\Input.csv'
input_file = 'Day_05\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Define the grid size based off of input
num_list = []
max_x = 0
max_y = 0
for line in lines:
    numbers = re.findall(r"\d+",line)
    x1 = numbers[0]
    y1 = numbers[1]
    x2 = numbers[2]
    y2 = numbers[3]
    num_list.append((int(x1), int(y1), int(x2), int(y2)))
    if int(x1) > max_x:
        max_x = int(x1)
    if int(x2) > max_x:
        max_x = int(x2)
    if int(y1) > max_y:
        max_y = int(y1)
    if int(y2) > max_y:
        max_y = int(y2)

def build_grid():
    grid = {}
    for y in range(0, max_y + 1):
        grid[y] = {}
        for x in range(0, max_x + 1):
            grid[y][x] = 0
    return grid

def straight_lines(inp, grid):
    result = 0
    for num in inp:
        x1 = min(num[0], num[2])
        x2 = max(num[0], num[2])
        y1 = min(num[1], num[3])
        y2 = max(num[1], num[3])
        if y1 == y2:
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
        elif x1 == x2:
            for y in range(y1, y2 + 1):
                grid[y][x1] += 1
    for y in grid:
        for x in grid[y]:
            if grid[y][x] > 1:
                result += 1
    return grid, result

def print_grid(grid):
    for y in grid:
        print_line = ''
        for x in grid[y]:
            if grid[y][x] == 0:
                print_line += '.'
            else:
                print_line += str(grid[y][x])
        print(print_line)

# Part 1
grid = build_grid()
grid, result = straight_lines(num_list, grid)
print("Part 1: " + str(result))

# Part 2
grid = build_grid()

for num in num_list:
    x1 = min(num[0], num[2])
    x2 = max(num[0], num[2])
    y1 = min(num[1], num[3])
    y2 = max(num[1], num[3])
    if y1 == y2:
        for x in range(x1, x2 + 1):
            grid[y1][x] += 1
    elif x1 == x2:
        for y in range(y1, y2 + 1):
            grid[y][x1] += 1
    elif abs(x2 - x1) / abs(y2 - y1) == 1:
        i = num[0]
        j = num[1]
        if num[1] > num[3] and num[0] > num[2]:
            while i >= num[2]:
                grid[j][i] += 1
                i -= 1
                j -= 1
        elif num[1] > num[3] and num[0] < num[2]:
            while i <= num[2] and j <= num[3]:
                grid[j][i] += 1
                i += 1
                j -= 1
        elif num[1] < num[3] and num[0] > num[2]:
            while i >= num[2] and j <= num[3]:
                grid[j][i] += 1
                i -= 1
                j += 1
        elif num[1] < num[3] and num[0] < num[2]:
            while i <= num[2] and j <= num[3]:
                grid[j][i] += 1
                i += 1
                j += 1

mult_ints = 0
for y in grid:
    print_line = ''
    for x in grid[y]:
        if grid[y][x] > 1:
            mult_ints += 1
        if grid[y][x] == 0:
            print_line += '.'
        else:
            print_line += str(grid[y][x])
    print(print_line)

print("Part 2: " + str(mult_ints))