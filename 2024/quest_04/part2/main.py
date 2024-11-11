FILENAME = "everybody_codes_e2024_q4_p2.txt"

with open(FILENAME) as f:
    heights = [int(height) for height in f.read().split('\n')]

min_height = min(heights)
strikes = 0
for height in heights:
    strikes += height - min_height
print(f"{strikes =}")
