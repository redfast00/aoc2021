import re
from itertools import chain

with open('input') as infile:
    bingo_order = [int(num) for num in infile.readline().strip().split(',')]
    text_boards = [board.strip() for board in infile.read().split('\n\n')]
    boards = [[[int(field) for field in re.split(' +', line.strip())] for line in board.split('\n')] for board in text_boards]

def create_winconditions(board):
    horizontal_winconditions = [set(line) for line in board]
    vertical_wincondidtions = [{line[idx] for line in board} for idx in range(len(board[0]))]
    return horizontal_winconditions + vertical_wincondidtions

def does_win(winconditions, called_numbers):
    return any(condition.issubset(called_numbers) for condition in winconditions)

def calculate_score(board, last_number, called_numbers):
    all_board_numbers = set(chain.from_iterable(board))
    only_unmarked = all_board_numbers - called_numbers
    return sum(only_unmarked) * last_number


boards_winconditions = [create_winconditions(b) for b in boards]

def solve_first():
    called_numbers = set()
    for elem in bingo_order:
        called_numbers.add(elem)
        for idx, winconditions in enumerate(boards_winconditions):
            if does_win(winconditions, called_numbers):
                return calculate_score(boards[idx], elem, called_numbers)

print(solve_first())

def solve_second():
    called_numbers = set()
    boards_still_playing = set(range(len(boards)))
    for elem in bingo_order:
        called_numbers.add(elem)
        for idx, winconditions in enumerate(boards_winconditions):
            if (idx not in boards_still_playing):
                continue
            if len(boards_still_playing) > 1 and does_win(winconditions, called_numbers):
                boards_still_playing.remove(idx)
            elif len(boards_still_playing) == 1 and does_win(winconditions, called_numbers):
                return calculate_score(boards[idx], elem, called_numbers)

print(solve_second())
