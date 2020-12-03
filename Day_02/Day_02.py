import re

input_file = 'Day_02\\Input.csv'
# input_file = 'Day_02\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def parse_lines(line):
    numbers = re.findall(r"\d+",line)
    lower = int(numbers[0])
    upper = int(numbers[1])
    char = line.split(' ')[1][0]
    password = line.split(' ')[2]
    return lower, upper, char, password

def count_letters_p1(line):
    lower, upper, char, password = parse_lines(line)
    num_char = password.count(char)
    if num_char in range(lower, upper + 1):
        return 1
    else:
        return 0

def count_letters_p2(line):
    lower, upper, char, password = parse_lines(line)
    lower -= 1
    upper -= 1
    if password[lower] == char:
        if password[upper] != char:
            return 1
        else:
            return 0
    elif password[upper] == char:
        if password[lower] !=char:
            return 1
        else:
            return 0
    else:
        return 0

def count_passwords_p1(lines):
    total = 0
    for line in lines:
        total += count_letters_p1(line)
    return total

def count_passwords_p2(lines):
    total = 0
    for line in lines:
        total += count_letters_p2(line)
    return total

print("Part 1: " + str(count_passwords_p1(lines)))
print("Part 2: " + str(count_passwords_p2(lines)))