input_file = 'Day_02\\Input.csv'
# input_file = 'Day_02\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def read_line(line):
    hor = 0
    vert = 0
    dir = line.split(' ')[0]
    if dir == 'forward':
        hor = int(line.split(' ')[1])
    elif dir == 'down':
        vert = int(line.split(' ')[1])
    elif dir == 'up':
        vert = int(line.split(' ')[1]) * -1
    return [hor, vert]


# Part 1
hor1 = 0
vert1 = 0
for line in lines:
    hor1 += read_line(line)[0]
    vert1 += read_line(line)[1]

# Part 2
hor2 = 0
vert2 = 0
aim = 0
for line in lines:
    hor2 += read_line(line)[0]
    aim += read_line(line)[1]
    if aim == 0:
        vert2 += 0
    else:
        vert2 += read_line(line)[0] * aim

print("Part 1: " + str(hor1 * vert1))
print("Part 2: " + str(hor2 * vert2))