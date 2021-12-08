input_file = 'Day_08\\Input.csv'
# input_file = 'Day_08\\Test.csv'
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

def part_1(line):
    result = 0
    inputs, code = read_input(line)
    for c in code:
        if len(c) == 2 or len(c) == 3 or len(c) == 4 or len(c) == 7:
            result += 1
    return result

def new_letters(line, letters):
    inputs, code = read_input(line)
    inputs.sort(key = len)
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    seen_letters = []
    for inp in inputs:
        if len(inp) == 2:
            for i in inp:
                letters["c"].append(i)
                letters["f"].append(i)
                if i not in seen_letters:
                    seen_letters.append(i)
        if len(inp) == 3:
            for i in inp:
                if i not in seen_letters:
                    letters["a"].append(i)
                    seen_letters.append(i)
        if len(inp) == 4:
            for i in inp:
                if i not in seen_letters:
                    letters["b"].append(i)
                    letters["d"].append(i)
                    seen_letters.append(i)
        if len(inp) == 6:
            count = 0
            for i in inp:
                if i in seen_letters:
                    count += 1
            if count == 5 and len(seen_letters) == 5:
                for i in inp:
                    if i not in seen_letters:
                        letters["g"].append(i)
                        seen_letters.append(i)
                letters["e"].append(list(set(all_letters) - set(seen_letters))[0])
    for inp in inputs:
        if len(inp) == 6 and len(letters["c"]) > 1:
            hunt = letters["c"]
            for h in range(0, 2):
                if hunt[h] not in inp:
                    letters["c"] = [hunt[h]]
                    if h == 0:
                        letters["f"] = [hunt[1]]
                    else:
                        letters["f"] = [hunt[0]]
    for inp in inputs:
        if len(inp) == 6 and len(letters["b"]) > 1:
            hunt = letters["b"]
            for h in range(0, 2):
                if hunt[h] not in inp:
                    letters["d"] = [hunt[h]]
                    if h == 0:
                        letters["b"] = [hunt[1]]
                    else:
                        letters["b"] = [hunt[0]]

def reset_key():
    lets = {
        "a": [],
        "b": [],
        "c": [],
        "d": [],
        "e": [],
        "f": [],
        "g": [] 
    }
    return lets
            
def replace_letters(line):
    key = reset_key().copy()
    new_digits = {}
    new_digits = digits.copy()
    new_code = []
    new_letters(line, key)
    key_list = list(key.keys())
    val_list = list(key.values())
    input, code = read_input(line)
    for cd in code:
        conv = ''
        for c in cd:
            pos = val_list.index([c])
            conv += key_list[pos]
        new_code.append(''.join(sorted(conv)))
    return new_code

def find_digits(line):
    code = replace_letters(line)
    key_list = list(digits.keys())
    val_list = list(digits.values())
    result = ''
    for cd in code:
        digit = ''
        pos = val_list.index(cd)
        digit += key_list[pos]
        result += digit
    return int(result)

def run_sum(lines):
    cum_sum = 0
    for line in lines:
        cum_sum += find_digits(line)
    return cum_sum

# Part 1
cum_sum = 0
for line in lines:
    cum_sum += part_1(line)

print("Part 1: " + str(cum_sum))
print("Part 2: " + str(run_sum(lines)))