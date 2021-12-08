# input_file = 'Day_08\\Input.csv'
input_file = 'Day_08\\Test.csv'
# input_file = 'Day_08\\Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

digits = {
    "0": 'abcefg',
    "1": 'cf',
    "2": 'acdeg',
    "3": 'acdfg',
    "4": 'bcdf',
    "5": 'abdfg',
    "6": 'abdefg',
    "7": 'acf',
    "8": 'abcdefg',
    "9": 'abcdfg'
}

letters = {
    "a": '',
    "b": '',
    "c": '',
    "d": '',
    "e": '',
    "f": '',
    "g": ''
}

def read_input(line):
    inputs = []
    code = []
    inps = line.split('|')[0].split(' ')
    outps = line.split('|')[1].split(' ')
    for inp in inps:
        if inp != '':
            inputs.append(inp)
    for outp in outps:
        if outp != '':
            code.append(outp)
    return inputs, code

def convert_letters(line):
    new_letters = {}
    new_letters = letters.copy()
    inputs, code = read_input(line)
    for inp in inputs:
        if len(inp) == 7:
            new_letters["a"]= inp[0]
            new_letters["b"]= inp[1]
            new_letters["c"]= inp[2]
            new_letters["d"]= inp[3]
            new_letters["e"]= inp[4]
            new_letters["f"]= inp[5]
            new_letters["g"]= inp[6]
    print(new_letters)
    print(inputs)

def part_1(line):
    result = 0
    inputs, code = read_input(line)
    for c in code:
        if len(c) == 2 or len(c) == 3 or len(c) == 4 or len(c) == 7:
            result += 1
    return result

new_digits = {}
new_digits = digits.copy()
# key_list = list(new_digits.keys())
# val_list = list(new_digits.values())
# pos = val_list.index('cf')
# print(key_list[pos])

# Part 1
cum_sum = 0
for line in lines:
    cum_sum += part_1(line)

print("Part 1: " + str(cum_sum))