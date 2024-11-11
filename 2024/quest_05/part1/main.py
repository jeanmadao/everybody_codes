FILENAME = "everybody_codes_e2024_q5_p1.txt"

with open(FILENAME) as f:
    grid = f.read().strip().split('\n')
    grid = [row.split(' ') for row in grid]
    columns = [[int(grid[i][j]) for i in range(len(grid))] for j in range(len(grid[0]))]

for k in range(10):
    clapper = columns[k % len(columns)].pop(0)
    columns[(k + 1) % len(columns)].insert(clapper - 1, clapper)
    for j in range(len(columns)):
        print(columns[j][0], end='')
    print()
