input_file = 'Day_14\\Input.csv'
# input_file = 'Day_14\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

elements = {}
counts = {}
for i in range(0, len(lines)):
    if i == 0:
        inp = lines[i]
    elif i > 1:
        maps = lines[i].split(' -> ')
        elements[maps[0]] = maps[1]

first_letter = inp[0]
last_letter = inp[len(inp) - 1]

def read_inp(inp):
    for i in range(0, len(inp) - 1):
        if inp[i] + inp[i + 1] in elements:
            counts[inp[i] + inp[i + 1]] = 1

def insert_element(counts):
    outp1 = ''
    outp2 = ''
    new_counts = counts.copy()
    for i in counts:
        if i in elements:
            outp1 = i[0] + elements[i]
            outp2 = elements[i] + i[1]
            if outp1 not in new_counts:
                new_counts[outp1] = 0
            if outp2 not in new_counts:
                new_counts[outp2] = 0
            new_counts[outp1] += counts[i]
            new_counts[outp2] += counts[i]
            new_counts[i] -= counts[i]
    return new_counts

def count_letters(counts):
    outp_letters = {}
    for c in counts:
        let1 = c[0]
        let2 = c[1]
        if let1 in outp_letters:
            outp_letters[let1] += counts[c]
        else:
            outp_letters[let1] = counts[c]
        if let2 in outp_letters:
            outp_letters[let2] += counts[c]
        else:
            outp_letters[let2] = counts[c]
    if outp_letters[first_letter] == max(outp_letters.values()) or outp_letters[last_letter] == max(outp_letters.values()):
        most = max(outp_letters.values()) / 2 + 1
    else:
        most = max(outp_letters.values()) / 2
    if outp_letters[first_letter] == min(outp_letters.values()) or outp_letters[last_letter] == min(outp_letters.values()):
        least = min(outp_letters.values()) / 2 + 1
    else:
        least = min(outp_letters.values()) / 2
    return most, least

read_inp(inp)

for i in range(0, 40):
    counts = insert_element(counts)
    most, least = count_letters(counts)
    if i == 9:
        print("Part 1: " + str(most - least))
        
print("Part 2: " + str(most - least))

