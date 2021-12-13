import re

# input_file = 'Day_13\\Input.csv'
input_file = 'Day_13\\Test.csv'
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
        max_x = 0
    if y > max_y:
        max_y = 0
    grid[y, x] = 'X'

def print_grid(grid):
    for y in range(0, max_y + 1):
        grid_line = ''
        for x in range(0, max_x + 1):
            if (y, x) not in grid:
                grid_line += '.'
            else:
                grid_line += grid[y, x]
        print(grid_line)

print_grid(grid)
