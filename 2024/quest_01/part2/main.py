FILENAME = "everybody_codes_e2024_q1_p2.txt"

total_potions = 0

with open(FILENAME) as f:
    sequence = f.read()
    for i in range(0, len(sequence), 2):
        pair = sequence[i:i+2]
        if not 'x' in pair:
            total_potions += 2
        for j in range(2):
            match pair[j]:
                case 'B':
                    total_potions += 1
                case 'C':
                    total_potions += 3
                case 'D':
                    total_potions += 5

print(f"{total_potions = }")
