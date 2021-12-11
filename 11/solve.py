from itertools import product
from collections import deque


with open('input') as infile:
    board = [[int(c) for c in line.strip()] for line in infile]

adjacents = set(product((-1, 0, 1), repeat=2)) - set([(0, 0)])


def step(board):
    flashes = 0
    positions = {
        (x, y): (board[x][y] + 1) for x in range(len(board)) for y in range(len(board[x]))
    }
    flash_level = deque(p for p, level in positions.items() if level >= 10)
    while flash_level:
        coordinate = (x, y) = flash_level.popleft()
        if positions[coordinate] == 0:
            continue
        flashes += 1
        positions[coordinate] = 0
        for (dx, dy) in adjacents:
            inc_coordinate = (x + dx, y + dy)
            if inc_coordinate not in positions or positions[inc_coordinate] == 0:
                continue
            positions[inc_coordinate] += 1
            if positions[inc_coordinate] >= 10:
                flash_level.append(inc_coordinate)
    return flashes, [[positions[(x,y)] for y in range(len(board[0]))] for x in range(len(board))]


totalflashes = 0
for _ in range(100):
    flashes, board = step(board)
    totalflashes += flashes
print(totalflashes)

steps = 100
while True:
    steps += 1
    flashes, board = step(board)
    if flashes == len(board) * len(board[0]):
        print(steps)
        break