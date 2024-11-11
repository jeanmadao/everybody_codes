FILENAME = "everybody_codes_e2024_q4_p3.txt"

with open(FILENAME) as f:
    heights = [int(height) for height in f.read().strip().split('\n')]

median_height = sorted(heights)[len(heights)//2]
strikes = 0
for height in heights:
    strikes += abs(height - median_height)

print(f"{strikes = }")
