FILENAME = "everybody_codes_e2024_q2_p3.txt"

def find_ranges(needle, haystack):
    ranges = []
    needle_len = len(needle)
    haystack_col_len = len(haystack)
    haystack_row_len = len(haystack[0])
    for i in range(len(haystack)):
        for j in range(haystack_row_len):
            k = 0
            r = []
            while k < needle_len and haystack[i][(j+k) % haystack_row_len] == needle[k]:
                r.append(i*haystack_row_len + (j+k) % haystack_row_len)
                k += 1
            if k == needle_len:
                ranges.append(r)

            k = 0
            r = []
            while k < needle_len and haystack[i][(j-k) % haystack_row_len] == needle[k]:
                r.append(i*haystack_row_len + (j-k) % haystack_row_len)
                k += 1
            if k == needle_len:
                ranges.append(r)

            if i + needle_len <= haystack_col_len:
                k = 0
                r = []
                while k < needle_len and haystack[i+k][j] == needle[k]:
                    r.append((i+k) * haystack_row_len + j)
                    k += 1
                if k == needle_len:
                    ranges.append(r)
            if i + 1 - needle_len >= 0:
                k = 0
                r = []
                while k < needle_len and haystack[i-k][j] == needle[k]:
                    r.append((i-k) * haystack_row_len + j)
                    k += 1
                if k == needle_len:
                    ranges.append(r)
    return ranges


nb_runic_words = 0

index_set = set()

with open(FILENAME) as f:
    runic_words = f.readline().strip().split(':')[1].split(',')
    f.readline()
    sequence = f.read().strip().split('\n')
    for runic_word in runic_words:
        ranges = find_ranges(runic_word, sequence)
        for r in ranges:
            index_set = index_set.union(r)

print(f"{len(index_set) = }")
