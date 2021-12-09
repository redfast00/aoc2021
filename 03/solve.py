from collections import Counter


with open('input') as infile:
    content = [line.strip() for line in infile]

input_size = len(content[0])

# 1
gamma = ''
for idx in range(input_size):
    c = Counter(l[idx] for l in content)
    gamma += c.most_common(1)[0][0]

gamma_int = int(gamma, 2)
epsilon = gamma.replace('0', '_').replace('1', '0').replace('_', '1')
epsilon_int = int(epsilon, 2)
print(gamma_int * epsilon_int)

# 2
def filter_common(candidates, invert):
    for idx in range(input_size):
        c = Counter(l[idx] for l in candidates)
        most_common = '1' if ((c['1'] >= c['0']) != invert) else '0'
        candidates = {candidate for candidate in candidates if (candidate[idx] == most_common)}
        if len(candidates) == 1:
            return next(iter(candidates))

oxygen = filter_common(content, False)
co2 = filter_common(content, True)

print(int(oxygen, 2) * int(co2, 2))
