from collections import Counter

with open('input') as infile:
    timers = [int(p) for p in infile.read().strip().split(',')]

def simulate_day(old):
    new = Counter()
    for age, amount in old.items():
        if age == 0:
            new[6] += amount
            new[8] += amount
        else:
            new[age - 1] += amount
    return new

# 1
current = Counter(timers)
for _ in range(80):
    current = simulate_day(current)

print(sum(current.values()))

# 2
current = Counter(timers)
for _ in range(256):
    current = simulate_day(current)

print(sum(current.values()))