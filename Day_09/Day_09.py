input_file = 'Day_09\\Input.csv'
# input_file = 'Day_09\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
max_y = len(lines)
max_x = len(lines[0])

def build_grid(lines):
    grid = {}
    for y in range(0, max_y):
        grid[y] = {}
        for x in range(0, max_x):
            grid[y][x] = lines[y][x]
    return grid

def print_grid(grid):
    for y in grid:
        print_line = ''
        for x in grid[y]:
            print_line += str(grid[y][x])
        print(print_line)

def check_up(grid, y, x):
    if y == 0:
        return 1
    elif int(grid[y][x]) < int(grid[y - 1][x]):
        return 1
    else:
        return 0

def check_down(grid, y, x):
    if y == max_y - 1:
        return 1
    elif int(grid[y][x]) < int(grid[y + 1][x]):
        return 1
    else:
        return 0

def check_left(grid, y, x):
    if x == 0:
        return 1
    elif int(grid[y][x]) < int(grid[y][x - 1]):
        return 1
    else:
        return 0

def check_right(grid, y, x):
    if x == max_x - 1:
        return 1
    elif int(grid[y][x]) < int(grid[y][x + 1]):
        return 1
    else:
        return 0

def risk_lowpoints(grid):
    cum_sum = 0
    low_x = []
    low_y = []
    for y in range(0, max_y):
        for x in range(0, max_x):
            temp_sum = check_down(grid, y, x) + check_up(grid, y, x) + check_left(grid, y, x) + check_right(grid, y, x)
            if temp_sum == 4:
                cum_sum += int(grid[y][x]) + 1
                low_y.append(y)
                low_x.append(x)
    return low_y, low_x, cum_sum

def check_basin(grid, basin_inp, y, x):
    orig_value = int(grid[y][x])
    new_basin = basin_inp
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
    
    if (y, x) not in new_basin:
        new_basin.append((y, x))

    for j in check_y:
        for i in check_x:
            if (y + j, x + i) not in new_basin:
                new_value = int(grid[y + j][x + i])
                if new_value > orig_value and new_value < 9:
                    new_basin.append((y + j, x + i))
    return new_basin
        

def calc_basin(grid):
    basin_size = []
    low_y, low_x, cum_sum = risk_lowpoints(grid)
    for i in range(0, len(low_y)):
        basin = []
        basin.append((low_y[i], low_x[i]))
        for b in basin:
            basin = check_basin(grid, basin, b[0], b[1])
        basin_size.append(len(basin))
    top_3 = sorted(basin_size, reverse = True)[:3]
    # print(basin_size)
    return top_3

def final_part2(grid):
    top_3 = calc_basin(grid)
    result = top_3[0] * top_3[1] * top_3[2]
    return result


grid = build_grid(lines)
low_y, low_x, cum_sum = risk_lowpoints(grid)
part2_mult = final_part2(grid)
print("Part 1: " + str(cum_sum))
print("Part 2: " + str(part2_mult))