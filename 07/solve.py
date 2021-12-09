with open('input') as infile:
    positions = [int(p) for p in infile.read().strip().split(',')]

minimal_movement = float('inf')
for align_position in range(min(positions), max(positions)):
    total_movement = sum(abs(align_position - pos) for pos in positions)
    minimal_movement = min(total_movement, minimal_movement)

print(minimal_movement)

def dist_fun(n):
    return (n*(n+1))//2

# 2

minimal_movement = float('inf')
for align_position in range(min(positions), max(positions)):
    total_movement = sum(dist_fun(abs(align_position - pos)) for pos in positions)
    minimal_movement = min(total_movement, minimal_movement)

print(minimal_movement)

