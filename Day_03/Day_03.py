# input_file = 'Day_03\\Input.csv'
input_file = 'Day_03\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

maxlength = len(lines[0])
print(maxlength)

# Part 1
num0 = []
num1 = []
gamma = ''
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
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gammaconv = int(gamma, 2)
epsilonconv = int(epsilon, 2)

print("Part 1: " + str(gammaconv * epsilonconv))

# Part 2