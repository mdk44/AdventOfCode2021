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

new_digits = {}
new_digits = digits.copy()

