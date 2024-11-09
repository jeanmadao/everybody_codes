FILENAME = "everybody_codes_e2024_q2_p2.txt"

def find_ranges(needle, haystack):
    ranges = []
    needle_len = len(needle)
    for i in range(len(haystack)):
        if i + needle_len <= len(haystack):
            j = 0
            while j < needle_len and haystack[i+j] == needle[j]:
                j += 1
            if j == needle_len:
                ranges.append(range(i, i+j))

        if i + 1 >= needle_len:
            j = 0
            while j < needle_len and haystack[i-j] == needle[j]:
                j += 1
            if j == needle_len:
                ranges.append(range(i-j + 1, i + 1))
    return ranges


nb_runic_words = 0

index_set = set()

with open(FILENAME) as f:
    runic_words = f.readline().strip().split(':')[1].split(',')
    f.readline()
    sequence = f.read()
    for runic_word in runic_words:
        ranges = find_ranges(runic_word, sequence)
        for r in ranges:
            index_set = index_set.union(r)

print(f"{len(index_set) = }")
