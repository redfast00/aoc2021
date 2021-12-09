with open('input') as infile:
    numbers = [int(line.strip()) for line in infile]

ctr = 0
for fst, snd in zip(numbers, numbers[1:]):
    if snd > fst:
        ctr += 1
print(ctr)
sctr = 0
for fst, snd, trd, frt in zip(numbers, numbers[1:], numbers[2:], numbers[3:]):
    if fst + snd + trd < snd + trd + frt:
        sctr += 1

print(sctr)