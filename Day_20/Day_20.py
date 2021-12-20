# input_file = 'Day_20\\Input.csv'
input_file = 'Day_20\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

inp = lines[0]

def build_grid(lines):
    grid = {}
    for y in range(2, len(lines)):
        grid[y] = {}
        for x in range(0, len(lines[y])):
            grid[y][x] = lines[y][x]
    return grid

def print_grid(grid):
    for y in grid:
        grid_line = ''
        for x in grid[y]:
            grid_line += grid[y][x]
        print(grid_line)

print_grid(build_grid(lines))