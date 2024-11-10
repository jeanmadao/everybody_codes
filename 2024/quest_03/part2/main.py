FILENAME = "everybody_codes_e2024_q3_p2.txt"

def dig_map(grid):
    diggable = True
    total_dug = 0
    height = len(grid)
    width = len(grid[0])
    while diggable:
        next_layer = [['.' for _ in range(width)] for _ in range(height)]
        layer_dug = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '#':
                    layer_dug += 1
                    if 0 < i < height - 1 and 0 < j < width - 1:
                        if grid[i-1][j] == '#' and grid[i+1][j] == '#' and grid[i][j-1] == '#' and grid[i][j+1] == '#':
                            next_layer[i][j] = '#'
        if layer_dug > 0:
            total_dug += layer_dug
            grid = next_layer
        else:
            diggable = False

    return total_dug


grid = []
with open(FILENAME) as f:
    row = f.readline().strip()
    while row:
        grid.append(list(row))
        row = f.readline().strip()
print(dig_map(grid))
