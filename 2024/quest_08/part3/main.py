FILENAME = "everybody_codes_e2024_q08_p3.txt"

with open(FILENAME) as f:
    notes = int(f.read().strip())

acolytes = 10
blocks_avail = 202400000
layer_width = 1
layer_thickness = 1
total = 0
thicknesses = []
while total < blocks_avail:
    thicknesses.append(layer_thickness)
    total += layer_width * layer_thickness

    layer_thickness = (layer_thickness * notes) % acolytes + acolytes
    layer_width += 2
layer_width -= 2

layer_thickness = thicknesses.pop()
while thicknesses:
    layer_thickness += thicknesses.pop()
    blocks_removed = 2 * (notes * layer_width * layer_thickness % acolytes)
    total -= blocks_removed
total += blocks_removed // 2

print(total - blocks_avail)
