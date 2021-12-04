# input_file = 'Day_04\\Input.csv'
input_file = 'Day_04\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

numcards = 0
for line in lines:
    if line == '':
        numcards += 1

bingocards = []
nums = map(int, lines[0].split(','))

x = 0
bingocards.append([])
for line in range(2, len(lines)):
    if lines[line] != '':
        bingocards[x].append(lines[line])
    else:
        x += 1
        bingocards.append([])

for x in range(0, len(bingocards[0])):
    print(bingocards[0][x])