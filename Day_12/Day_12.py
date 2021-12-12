# input_file = 'Day_12\\Input.csv'
input_file = 'Day_12\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Here's how I would do it:
# create a loop that builds multiple lists with all possibilities, then delete each one that either doesn't hit the end or has to cross a lowercase twice
# build a list of lowercase strings and remove them as you cross them
# Experiment with an __init__ and self function setup

connections = {}
lowercases = []
for line in lines:
    p1 = line.split('-')[0]
    p2 = line.split('-')[1]
    if p1 not in connections:
        connections[p1] = [p2]
    if p2 not in connections:
        connections[p2] = [p1]
    if p2 not in connections[p1]:
        connections[p1].append(p2)
    if p1 not in connections[p2]:
        connections[p2].append(p1)
    if p1.islower() and p1 not in lowercases:
        lowercases.append(p1)
    if p2.islower() and p2 not in lowercases:
        lowercases.append(p2)

def generate_path(lowers):
    l = lowers[:]
    paths = []
    for p in connections['start']:
        paths.append(connections[p])
    l.remove('start')
    print(paths)
    print(l)

generate_path(lowercases)
print(lowercases)

