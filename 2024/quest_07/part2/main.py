FILENAME = "everybody_codes_e2024_q07_p2.txt"
TRACK_FILENAME = "track"

count = {}

track = ""
with open(TRACK_FILENAME) as f:
    content = f.read().strip()
    content = content.split('\n')
    track += content[0][1:]
    for i in range(1, len(content) - 1):
        track += content[i][-1]
    track += content[-1][::-1]
    for i in range(len(content) - 2, 0, -1):
        track += content[i][0]
    track += 'S'

with open(FILENAME) as f:
    line = f.readline()
    while line:
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
        count[char] = total
        line = f.readline()
res = sorted(count.items(), key=lambda x:x[1], reverse=True)
print(*[char[0] for char in res], sep='')
