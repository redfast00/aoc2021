from collections import Counter
from pprint import pprint

with open('input') as infile:
    connections = [((spl := line.strip().split('-'))[0], spl[1]) for line in infile]
    connections.extend([(snd, fst) for fst, snd in connections])

def from_here(current_point, used):
    result = []
    for fst, snd in connections:
        if fst == current_point:
            if snd == 'end':
                result.append(['end'])
            elif snd not in used:
                new_used = used | {snd} if snd.lower() == snd else used
                paths = from_here(snd, new_used)
                result.extend([current_point] + path for path in paths)
    return result

print(len(from_here('start', {'start'})))

def from_here_2(current_point, used, visit_twice_used):
    result = []
    for fst, snd in connections:
        if fst == current_point:
            if snd == 'end':
                result.append([snd])
            elif snd == 'start':
                pass
            elif snd not in used or snd.upper() == snd:
                new_used = used
                if snd.lower() == snd:
                    new_used = used | {snd}
                paths = from_here_2(snd, new_used, visit_twice_used)
                result.extend([snd] + path for path in paths)
            elif snd in used and snd.lower() == snd and not visit_twice_used:
                new_used = used | {snd}
                paths = from_here_2(snd, new_used, True)
                result.extend([snd] + path for path in paths)
    return result

print(len(from_here_2('start', {'start', 'end'}, False)))