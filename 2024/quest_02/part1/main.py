FILENAME = "everybody_codes_e2024_q2_p1.txt"

nb_runic_words = 0

with open(FILENAME) as f:
    runic_words = f.readline().strip().split(':')[1].split(',')
    f.readline()
    sequence = f.readline()
    print(runic_words)
    print(sequence)
    for runic_word in runic_words:
        print(runic_word)
        nb_runic_words += sequence.count(runic_word)
        print(nb_runic_words)
print(f"{nb_runic_words = }")
