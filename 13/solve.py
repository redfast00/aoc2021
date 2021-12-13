with open('secret') as infile:
    coordinates, instructions = infile.read().strip().split('\n\n')
    coordinates = [tuple(int(p) for p in line.split(',')) for line in coordinates.split('\n')]
    instructions = [tuple(line.split(' ')[-1].split('=')) for line in instructions.split('\n')]

    instructions = [(axis, int(c)) for axis, c in instructions]


def mirror(instruction, board):
    newboard = {}
    axis, axis_number = instruction
    for (x, y), value in board.items():
        nx, ny = x, y
        if axis == 'x':
            nx = x if x < axis_number else axis_number - (x - axis_number)
        else:
            ny = y if y < axis_number else axis_number - (y - axis_number)
        newboard[(nx, ny)] = value
    return newboard

board = {(x, y): True for (x, y) in coordinates}
print(len(mirror(instructions[0], board).values()))

for instruction in instructions:
    board = mirror(instruction, board)

max_x = max(x for x,y in board.keys())
max_y = max(y for x,y in board.keys())

print('\n'.join(''.join('#' if board.get((x,y), False) else ' ' for x in range(max_x+1)) for y in range(max_y+1)))
