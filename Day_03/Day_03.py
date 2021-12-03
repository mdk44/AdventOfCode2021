input_file = 'Day_03\\Input.csv'
# input_file = 'Day_03\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

maxlength = len(lines[0])

def find_gamma(lines):
    num0 = []
    num1 = []
    gamma = ''
    for x in range(0, maxlength):
        num0.append(0)
        num1.append(0)

    for line in lines:
        for x in range(0, maxlength):
            if int(line[x]) == 0:
                num0[x] += 1
            elif int(line[x]) == 1:
                num1[x] += 1

    for x in range(0, maxlength):
        if num0[x] > num1[x]:
            gamma += '0'
            # epsilon += '1'
        else:
            gamma += '1'
            # epsilon += '0'
    return gamma

def find_epsilon(lines):
    num0 = []
    num1 = []
    epsilon = ''
    for x in range(0, maxlength):
        num0.append(0)
        num1.append(0)

    for line in lines:
        for x in range(0, maxlength):
            if int(line[x]) == 0:
                num0[x] += 1
            elif int(line[x]) == 1:
                num1[x] += 1

    for x in range(0, maxlength):
        if num0[x] > num1[x]:
            epsilon += '1'
        else:
            epsilon += '0'
    return epsilon

# Part 1
gammaconv = int(find_gamma(lines), 2)
epsilonconv = int(find_epsilon(lines), 2)
print("Part 1: " + str(gammaconv * epsilonconv))

# Part 2
temp_lines = lines
x = 0
while len(temp_lines) > 1:
    new_lines = []
    for line in temp_lines:
        if line[x] == find_gamma(temp_lines)[x]:
            new_lines.append(line)
    temp_lines = new_lines
    x += 1
gammaconv = int(new_lines[0], 2)

temp_lines = lines
x = 0
while len(temp_lines) > 1:
    new_lines = []
    for line in temp_lines:
        if line[x] == find_epsilon(temp_lines)[x]:
            new_lines.append(line)
    temp_lines = new_lines
    x += 1
epsilonconv = int(new_lines[0], 2)

print("Part 2: " + str(gammaconv * epsilonconv))