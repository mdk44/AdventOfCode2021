input_file = 'Day_11\\Input.csv'
# input_file = 'Day_11\\Test.csv'
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
        
def adjacent_points(y, x):
    return [(y + j, x + i) for j in range(-1, 2) for i in range(-1, 2) if (j, i) != (0, 0) and 0 <= y + j <= 9 and 0 <= x + i <= 9]

def flash_point(grid, y, x):
    grid[y][x] = 0
    for j, i in adjacent_points(y, x):
        if grid[j][i] != 0:
            grid[j][i] += 1
        if grid[j][i] > 9:
            grid[j][i] = 0
            flash_point(grid, j, i)

def flash_grid(grid):
    flashes = 0
    increase_energy(grid)
    for y in range(0, max_y):
        for x in range(0, max_x):
            if grid[y][x] > 9:
                flash_point(grid, y, x)

def find_zeros(grid):
    flashes = 0
    for y in range(0, max_y):
        for x in range(0, max_x):
            if grid[y][x] == 0:
                flashes += 1
    return flashes

grid = build_grid(lines)

flashes = 0
for i in range(1, 1000):
    flash_grid(grid)
    flashes += find_zeros(grid)
    if i == 100:
        print("Part 1: " + str(flashes))
    if find_zeros(grid) == 100:
        print("Part 2: " + str(i))
        break

