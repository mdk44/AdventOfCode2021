import re

# input_file = 'Day_05\\Input.csv'
input_file = 'Day_05\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

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

grid = {}
for y in range(0, max_y + 1):
    grid[y] = {}
    for x in range(0, max_x + 1):
        grid[y][x] = 0

for num in num_list:
    for y in range(num[1], num[3]):
        for x in range(num[0], num[2]):
            grid[y][x] += 1

for y in grid:
    print_line = ''
    for x in grid[y]:
        print_line += str(grid[y][x])
    print(print_line)