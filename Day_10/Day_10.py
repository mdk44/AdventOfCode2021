input_file = 'Day_10\\Input.csv'
# input_file = 'Day_10\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def remove_chunks(line):
    new_line = line
    done = 0
    while done != 1:
        if '()' not in new_line and '[]' not in new_line and '{}' not in new_line and '<>' not in new_line:
            done = 1
        else:
            new_line = new_line.replace('()', '')
            new_line = new_line.replace('[]', '')
            new_line = new_line.replace('{}', '')
            new_line = new_line.replace('<>', '')
    return new_line

def find_closer(line):
    new_line = remove_chunks(line)
    for i in range(0, len(new_line)):
        if new_line[i] == ')':
            return 3
        elif new_line[i] == ']':
            return 57
        elif new_line[i] == '}':
            return 1197
        elif new_line[i] == '>':
            return 25137
    return 0

def close_line(line):
    scores = []
    cum_sum = 0
    new_line = remove_chunks(line)
    while len(new_line) > 0:
        if new_line[len(new_line) - 1] in (')', ']', '}', '>'):
            return 0
        if new_line[len(new_line) - 1] == '(':
            new_line = new_line[:len(new_line) - 1]
            scores.append(1)
        elif new_line[len(new_line) - 1] == '[':
            new_line = new_line[:len(new_line) - 1]
            scores.append(2)
        elif new_line[len(new_line) - 1] == '{':
            new_line = new_line[:len(new_line) - 1]
            scores.append(3)
        elif new_line[len(new_line) - 1] == '<':
            new_line = new_line[:len(new_line) - 1]
            scores.append(4)
    for s in scores:
        cum_sum = cum_sum * 5 + s
    return cum_sum

def median(inp):
    new_list = sorted(inp)
    length = len(inp)
    index = (length - 1) // 2
   
    if (length % 2):
        return new_list[index]
    else:
        return (new_list[index] + new_list[index + 1]) / 2.0

def sum_part_1(lines):
    cum_sum = 0
    for line in lines:
        cum_sum += find_closer(line)
    return cum_sum

def sum_part_2(lines):
    scores = []
    for line in lines:
        score = close_line(line)
        if score != 0:
            scores.append(score)
    return median(scores)

print("Part 1: " + str(sum_part_1(lines)))
print("Part 2: " + str(sum_part_2(lines)))
