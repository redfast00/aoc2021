from collections import Counter
import functools
import operator

with open('input') as infile:
    board = [[int(c) for c in line.strip()] for line in infile]

def is_lower_than_ajacent(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx in range(len(board)) and ny in range(len(board[nx])) and board[x][y] >= board[nx][ny]:
            break
    else:
        return True
    return False

# 1
total_risk = 0
for x in range(len(board)):
    for y in range(len(board[x])):
        if is_lower_than_ajacent(x, y):
            total_risk += board[x][y] + 1
print(total_risk)

# 2
# map of coordinates to the coordinate adjacent that's lower
basin_coordinates = {}
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y] == 9:
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx in range(len(board)) and ny in range(len(board[nx])) and board[x][y] > board[nx][ny]:
                basin_coordinates[(x, y)] = (nx, ny)
                break
        else:
            basin_coordinates[(x, y)] = (x, y)

def lookup_lowpoint(coordinate):
    new_coordinate = basin_coordinates[coordinate]
    while coordinate != new_coordinate:
        coordinate = new_coordinate
        new_coordinate = basin_coordinates[coordinate]
    return new_coordinate

c = Counter()
for coordinate in basin_coordinates:
    c[lookup_lowpoint(coordinate)] += 1

print(functools.reduce(operator.mul, (e[1] for e in c.most_common(3))))
