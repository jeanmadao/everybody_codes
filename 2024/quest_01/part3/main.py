FILENAME = "everybody_codes_e2024_q1_p3.txt"

total_potions = 0

with open(FILENAME) as f:
    sequence = f.read().strip()
    for i in range(0, len(sequence), 3):
        trio = sequence[i:i+3]
        nb_x = trio.count('x')
        total_potions += (2 - nb_x) * (3 - nb_x)
        for j in range(3):
            match trio[j]:
                case 'B':
                    total_potions += 1
                case 'C':
                    total_potions += 3
                case 'D':
                    total_potions += 5


print(f"{total_potions = }")
