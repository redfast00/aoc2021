import statistics

open_to_close = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
}
opening_chars = set(open_to_close.keys())
closing_chars = set(open_to_close.values())

with open('input') as infile:
    lines = [l.strip() for l in infile]

score_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
uncorrupted = []
for line in lines:
    stack = []
    for char in line:
        if char in opening_chars:
            stack.append(char)
        else:
            expected = open_to_close[stack.pop()]
            if char != expected:
                score += score_dict[char]
                break
    else:
        uncorrupted.append(line)
print(score)

completion_score_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for line in uncorrupted:
    stack = []
    for char in line:
        if char in opening_chars:
            stack.append(char)
        else:
            stack.pop()
    completion = [open_to_close[c] for c in stack[::-1]]
    score = 0
    for char in completion:
        score *= 5
        score += completion_score_dict[char]
    scores.append(score)
print(statistics.median(scores))
