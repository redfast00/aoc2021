from collections import defaultdict
import heapq


with open('input') as infile:
    board = {
        (x, y): int(risk) for x, l in enumerate(line.strip() for line in infile) for y, risk in enumerate(l)
    }

adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solve(board):
    goal = max(board)
    visited = set()
    distances = defaultdict(lambda: float('inf'))
    previous = {} # turns out this was not needed
    explore_queue = []
    heapq.heappush(explore_queue, (0, (0, 0)))
    distances[(0, 0)] = 0
    while explore_queue:
        _, (x, y) = _, current = heapq.heappop(explore_queue)
        if current in visited:
            continue
        for dx, dy in adjacent:
            neighbour = dx + x, dy + y
            if neighbour in board and neighbour not in visited:
                if distances[neighbour] > distances[current] + board[neighbour]:
                    distances[neighbour] = distances[current] + board[neighbour]
                    previous[neighbour] = current
                    heapq.heappush(explore_queue, (distances[neighbour], neighbour))
        visited.add(current)
        if current == goal:
            break
    return distances[goal]

print(solve(board))
max_x, max_y = max(board)
len_x, len_y = max_x + 1, max_y + 1
newboard = {
    (x, y): (board[(x % len_x, y % len_y)] + (y // len_x) + (x // len_x) - 1) % 9 + 1
    for x in range(5 * len_x)
    for y in range(5 * len_y)
}
print(solve(newboard))

