FILENAME = "everybody_codes_e2024_q08_p2.txt"

with open(FILENAME) as f:
    notes = int(f.read().strip())

acolytes = 1111
blocks_avail = 20240000
layer_width = 1
layer_thickness = 1
total = 0
while total < blocks_avail:
    total += layer_width * layer_thickness
    layer_thickness = layer_thickness * notes % acolytes
    layer_width += 2
layer_width -= 2
print(layer_width * (total - blocks_avail))
