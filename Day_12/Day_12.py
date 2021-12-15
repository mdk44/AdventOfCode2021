input_file = 'Day_12\\Input.csv'
# input_file = 'Day_12\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

connections = {}
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

del connections['end']
for c in connections:
    if 'start' in connections[c]:
        connections[c].remove('start')

def generate_path(path = ['start']):
    paths = 0
    for p in connections[path[-1]]:
        if p.isupper() or p not in path:
            paths += 1 if p == 'end' else generate_path(path + [p])
    return paths

def generate_p2(path = ['start']):
    paths = 0
    for p in connections[path[-1]]:
        paths += 1 if p == 'end' else (generate_p2, generate_path)[p.islower() and p in path](path + [p])
    return paths

print("Part 1: " + str(generate_path()))
print("Part 2: " + str(generate_p2()))
