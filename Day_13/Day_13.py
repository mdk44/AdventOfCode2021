import re

input_file = 'Day_13\\Input.csv'
# input_file = 'Day_13\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

grid = {}
max_x = 0
max_y = 0
for line in lines:
    if line == '':
        break
    numbers = re.findall(r"\d+",line)
    x = int(numbers[0])
    y = int(numbers[1])
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    grid[y, x] = 'O '

for y in range(0, max_y + 1):
    for x in range(0, max_x + 1):
        if (y, x) not in grid:
            grid[y, x] = '  '

fold_dir = []
fold_num = []
for line in lines:
        if line[:4] == 'fold':
            numbers = re.findall(r"\d+",line)
            fold_num.append(int(numbers[0]))
            if 'x' in line:
                fold_dir.append('x')
            elif 'y' in line:
                fold_dir.append('y')

def print_grid(grid, num_y, num_x):
    for y in range(0, num_y + 1):
        grid_line = ''
        for x in range(0, num_x + 1):
            grid_line += grid[y, x]
        print(grid_line)

def count_points(grid, num_y, num_x):
    points = 0
    for y in range(0, num_y + 1):
        for x in range(0, num_x + 1):
            if grid[y, x] == 'O ':
                points += 1
    return points

def fold(grid, type, num):
    if type == 'y': # Horizontal
        for x in range(0, max_x + 1):
            grid[num, x] = '-'
        for y in range(0, num):
            for x in range(0, max_x + 1):
                if grid[y, x] == '  ' and (2 * num - y, x) in grid:
                    grid[y, x] = grid[2 * num - y, x]
        for y in range(num, max_y):
            for x in range(0, max_x + 1):
                del grid[y, x]
        new_y = num - 1
        new_x = max_x
    elif type == 'x': # Vertical
        for y in range(0, max_y + 1):
            grid[y, num] = '|'
        for y in range(0, max_y + 1):
            for x in range(0, num):
                if grid[y, x] == '  ' and (y, 2 * num - x) in grid:
                    grid[y, x] = grid[y, 2 * num - x]
        for y in range(0, max_y + 1):
            for x in range(num, max_x):
                del grid[y, x]
        new_y = max_y
        new_x = num - 1
    return new_y, new_x

for i in range(0, len(fold_dir)):
    max_y, max_x = fold(grid, fold_dir[i], fold_num[i])
    if i == 0: # Part 1
        print("Part 1: " + str(count_points(grid, max_y, max_x)))

print("Part 2:")
print_grid(grid, max_y, max_x)