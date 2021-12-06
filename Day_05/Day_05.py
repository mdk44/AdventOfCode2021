# input_file = 'Day_05\\Input.csv'
input_file = 'Day_05\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def print_grid(grid):
    for y in grid:
        grid_line = ''
        for x in grid[y]:
            grid_line.append(str(grid[y][x]))
        print(grid_line)

grid = {}
for y in range(0, 4):
    grid[y] = {}
    for x in range(0, 4):
        grid[y][x] = x

print_grid(grid)