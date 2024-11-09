FILENAME = "everybody_codes_e2024_q1_p1.txt"

total_potions = 0

with open(FILENAME) as f:
    sequence = f.read()
    for char in sequence:
        match char:
            case 'B':
                total_potions += 1
            case 'C':
                total_potions += 3

print(f"{total_potions = }")
