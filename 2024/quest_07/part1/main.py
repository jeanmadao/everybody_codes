FILENAME = "everybody_codes_e2024_q07_p1.txt"

count = {}

with open(FILENAME) as f:
    line = f.readline()
    while line:
        total = 0
        curr = 10
        char, ops = line.split(':')
        ops = ops.split(',')
        for i in range(10):
            match ops[i % len(ops)]:
                case '+':
                    curr += 1
                case '-':
                    curr -= 1
            total += curr
        count[char] = total
        line = f.readline()
res = sorted(count.items(), key=lambda x:x[1], reverse=True)
print(*[char[0] for char in res], sep='')
