# input_file = 'Day_11\\Input.csv'
input_file = 'Day_11\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

max_y = len(lines)
max_x = len(lines[0])

def build_grid(lines):
    grid = {}
    for y in range(0, max_y):
        grid[y] = {}
        for x in range(0, max_x):
            grid[y][x] = int(lines[y][x])
    return grid

def print_grid(grid):
    for y in grid:
        print_line = ''
        for x in grid[y]:
            print_line += str(grid[y][x])
        print(print_line)
    print('')

def increase_energy(grid):
    for y in range(0, max_y):
        for x in range(0, max_x):
            grid[y][x] += 1

def flash_point(grid, y, x):
    if y == 0:
        check_y = [0, 1]
    elif y == max_y - 1:
        check_y = [-1, 0]
    else:
        check_y = [-1, 0, 1]
    if x == 0:
        check_x = [0, 1]
    elif x == max_x - 1:
        check_x = [-1, 0]
    else:
        check_x = [-1, 0, 1]
    if grid[y][x] > 9:
        grid[y][x] == 0
        for j in range(0, len(check_y)):
            for i in range(0, len(check_x)):
                new_y = check_y[j]
                new_x = check_x[i]
                if grid[y + new_y][x + new_x] != 0:
                    grid[y + new_y][x + new_x] += 1

def flash_grid(grid):
    for y in range(0, max_y):
        for x in range(0, max_x):
            if grid[y][x] > 9:
                flash_point(grid, y, x)

grid = build_grid(lines)
increase_energy(grid)
flash_grid(grid)
increase_energy(grid)
flash_grid(grid)

