import re

input_file = 'Day_05\\Input.csv'
# input_file = 'Day_05\\Test.csv'
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
    new_grid = grid.copy()
    result = 0
    for num in inp:
        x1 = min(num[0], num[2])
        x2 = max(num[0], num[2])
        y1 = min(num[1], num[3])
        y2 = max(num[1], num[3])
        if y1 == y2:
            for x in range(x1, x2 + 1):
                new_grid[y1][x] += 1
        elif x1 == x2:
            for y in range(y1, y2 + 1):
                new_grid[y][x1] += 1
    for y in grid:
        for x in new_grid[y]:
            if new_grid[y][x] > 1:
                result += 1
    return new_grid, result

def diagonals(inp, grid):
    new_grid = grid.copy()
    result = 0
    for num in inp:
        x1 = num[0]
        x2 = num[2]
        y1 = num[1]
        y2 = num[3]
        if abs(y1 - y2) != 0 and abs(x1 - x2) / abs(y1 - y2) == 1:
            i = x1
            j = y1
            if x1 > x2 and y1 > y2:
                while i >= x2:
                    new_grid[j][i] += 1
                    i -= 1
                    j -= 1
            elif x1 < x2 and y1 > y2:
                while i <= x2:
                    new_grid[j][i] += 1
                    i += 1
                    j -= 1
            elif x1 > x2 and y1 < y2:
                while i >= x2:
                    new_grid[j][i] += 1
                    i -= 1
                    j += 1
            elif x1 < x2 and y1 < y2:
                while i <= x2:
                    new_grid[j][i] += 1
                    i += 1
                    j += 1
    for y in new_grid:
        for x in new_grid[y]:
            if new_grid[y][x] > 1:
                result += 1
    return new_grid, result
    

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
grid, result = straight_lines(num_list, grid)
grid, result = diagonals(num_list, grid) # everything up to THIS POINT is working peachy, so need to reconfigure diagonal function
print("Part 2: " + str(result))
# print_grid(grid)