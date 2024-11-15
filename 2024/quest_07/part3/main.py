FILENAME = "everybody_codes_e2024_q07_p3.txt"
TRACK_FILENAME = "track"

with open(TRACK_FILENAME) as f:
    content = f.read().rstrip()
    grid = content.split('\n')
    columns = 0
    for i in range(len(grid)):
        columns = max(len(grid[i]), columns)
    for i in range(len(grid)):
        grid[i] = grid[i] + (columns - len(grid[i])) * ' '

track = grid[0][1]
last_pos = (0, 0)
curr_pos = (0, 1)
while curr_pos != (0, 0):
    found = False
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    k = 0
    while not found and k < len(pos):
        next_i, next_j = (curr_pos[0] + pos[k][0], curr_pos[1] + pos[k][1])
        if (next_i, next_j) != last_pos and 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] != ' ':
            track += grid[next_i][next_j]
            found = True
            last_pos = curr_pos
            curr_pos = (next_i, next_j)
        k += 1
print(track)


with open(FILENAME) as f:
    line = f.readline()
    total = 0
    curr = 10
    char, ops = line.split(':')
    ops = ops.split(',')
    for i in range(len(track) * 2024):
        match track[i % len(track)].strip():
            case '=':
                match ops[i % len(ops)].strip():
                    case '+':
                        curr += 1
                    case '-':
                        curr -= 1
            case 'S':
                match ops[i % len(ops)].strip():
                    case '+':
                        curr += 1
                    case '-':
                        curr -= 1
            case '+':
                curr += 1
            case '-':
                curr -= 1
        total += curr
score_to_beat = total

def backtrack(track, score_to_beat, ops="", plus=5, minus=3, equal=3, count=0):
    if len(ops) == 11:
        total = 0
        curr = 10
        print(ops, count)
        for i in range(len(track) * 2024):
            match track[i % len(track)].strip():
                case '=':
                    match ops[i % len(ops)].strip():
                        case '+':
                            curr += 1
                        case '-':
                            curr -= 1
                case 'S':
                    match ops[i % len(ops)].strip():
                        case '+':
                            curr += 1
                        case '-':
                            curr -= 1
                case '+':
                    curr += 1
                case '-':
                    curr -= 1
            total += curr
        if total > score_to_beat:
            count += 1
    else:
        if plus > 0:
            count = backtrack(track, score_to_beat, ops + '+', plus - 1, minus, equal, count)
        if minus > 0:
            count = backtrack(track, score_to_beat, ops + '-', plus, minus -1, equal, count)
        if equal > 0:
            count = backtrack(track, score_to_beat, ops + '=', plus, minus, equal - 1, count)
    return count

count = backtrack(track, score_to_beat)
print(f"{count = }")
