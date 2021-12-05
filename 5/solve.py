from collections import Counter

with open('input') as infile:
    lines = []
    for line in infile:
        coords = line.strip().split(' -> ')
        p1 = coords[0].split(',')
        p2 = coords[1].split(',')
        lines.append(((int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))))

horizontal_or_vertical_lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]

def find_step(fst, snd):
    if fst == snd:
        return 0
    elif fst < snd:
        return 1
    else:
        return -1

def interpolate(l):
    step = (find_step(l[0][0], l[1][0]), find_step(l[0][1], l[1][1]))
    current = l[0]
    while current != l[1]:
        yield current
        current = (current[0] + step[0], current[1] + step[1])
    yield l[1]

# 1
c = Counter()
for line in horizontal_or_vertical_lines:
    c.update(interpolate(line))

print(len([k for k,v in c.items() if v > 1]))

# 2
c = Counter()
for line in lines:
    c.update(interpolate(line))

print(len([k for k,v in c.items() if v > 1]))
