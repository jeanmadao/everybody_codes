FILENAME = "everybody_codes_e2024_q08_p1.txt"

with open(FILENAME) as f:
    blocks_avail = int(f.read().strip())

layer_width = 1
layer_thickness = 1
total = 0
while total < blocks_avail:
    total += layer_width * layer_thickness
    layer_width += 2
layer_width -= 2
print(layer_width * (total - blocks_avail))
