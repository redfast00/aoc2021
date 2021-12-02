
vector_map = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1)
}

with open('input') as infile:
    actions = [((p := line.strip().split())[0], int(p[1])) for line in infile.readlines()]

# 1

position = 0
depth = 0

for (direction, amount) in actions:
    vec = vector_map[direction]
    position, depth = (position + vec[0] * amount, depth + vec[1] * amount)

print(position * depth)

# 2

# the existing map structure is not really useful for this, but we'll use it anyways

position = 0
depth = 0
aim = 0

for (direction, amount) in actions:
    vec = vector_map[direction]
    position = position + amount * vec[0]
    aim = aim + amount * vec[1]
    depth = depth + vec[0] * amount * aim

print(position * depth)

