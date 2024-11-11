FILENAME = "everybody_codes_e2024_q05_p3.txt"

with open(FILENAME) as f:
    grid = f.read().strip().split('\n')
    grid = [row.split(' ') for row in grid]
    columns = [[int(grid[i][j]) for i in range(len(grid))] for j in range(len(grid[0]))]

dancing = True
snapshots = []
k = 0

number = ""
for j in range(len(columns)):
    number += str(columns[j][0])

while dancing:
    curr_col_index = k % len(columns)
    snapshot = (int(number), curr_col_index, [[columns[i][j] for j in range(len(columns[0]))] for i in range(len(columns))])

    if snapshot not in snapshots:
        snapshots.append(snapshot)
    else:
        dancing = False
    next_col_index = (k + 1) % len(columns)
    clapper = columns[curr_col_index].pop(0)
    if (clapper - 1) // len(columns[next_col_index]) % 2 == 0:
        columns[next_col_index].insert((clapper - 1) % len(columns[next_col_index]), clapper)
    else:
        columns[next_col_index].insert(len(columns[next_col_index]) - (clapper - 1) % len(columns[next_col_index]), clapper)
    number = ""
    for j in range(len(columns)):
        number += str(columns[j][0])
    k += 1

print(f"{max(snapshots)[0] = }")
