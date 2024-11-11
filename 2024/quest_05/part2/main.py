FILENAME = "everybody_codes_e2024_q5_p2.txt"

with open(FILENAME) as f:
    grid = f.read().strip().split('\n')
    grid = [row.split(' ') for row in grid]
    columns = [[int(grid[i][j]) for i in range(len(grid))] for j in range(len(grid[0]))]

dancing = True

shouts = {}

k = 0
while dancing:
    curr_col_index = k % len(columns)
    next_col_index = (k + 1) % len(columns)
    clapper = columns[curr_col_index].pop(0)
    if (clapper - 1) // len(columns[next_col_index]) % 2 == 0:
        columns[next_col_index].insert((clapper - 1) % len(columns[next_col_index]), clapper)
    else:
        columns[next_col_index].insert(len(columns[next_col_index]) - (clapper - 1) % len(columns[next_col_index]), clapper)
    number = ""
    for j in range(len(columns)):
        number += str(columns[j][0])
    shouts[number] = shouts.get(number, 0) + 1
    if shouts[number] == 2024:
        dancing = False
    k += 1

print(f"{number = }")
print(f"{k = }")
print(f"{int(number) * k = }")
