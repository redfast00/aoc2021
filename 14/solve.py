from collections import Counter, defaultdict


with open('input') as infile:
    lines = [l.strip() for l in infile.readlines()]
    begin_polymer = lines[0]
    rules = [tuple(line.split(' -> ')) for line in lines[2:]]
    rules = {f: t for f, t in rules}

def step(polymer, rules):
    result = ''
    for a, b in zip(polymer, polymer[1:]):
        result = result + a + rules.get(a + b, '')
    result = result + polymer[-1]
    return result

polymer = begin_polymer
for _ in range(10):
    polymer = step(polymer, rules)
c = Counter(polymer)
print(c[max(c, key=c.get)] - c[min(c, key=c.get)])

def step_efficient(pair_count, rules):
    result = Counter()
    for pair, amount in pair_count.items():
        a, b = pair
        if pair in rules:
            c = rules[pair]
            result[a+c] += amount
            result[c+b] += amount
        else:
            result[pair] += amount
    return result

pair_count = Counter(a+b for a, b in zip(begin_polymer, begin_polymer[1:]))
for _ in range(40):
    pair_count = step_efficient(pair_count, rules)
base_counter = defaultdict(lambda: 0)
for (a,b), amount in pair_count.items():
    base_counter[a] += amount
base_counter[begin_polymer[-1]] += 1
print(base_counter[max(base_counter, key=base_counter.get)] - base_counter[min(base_counter, key=base_counter.get)])
