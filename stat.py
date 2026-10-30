import os

DIR_SRC = "src/"

map_word = {}

for fname in os.listdir(DIR_SRC):
    if ".tex" in fname:
        with open(DIR_SRC + fname, "r") as file:
            for word in file.read().replace('\n', ' ').split(' '):
                word = word.rstrip(",.:;").lower()
                if word != "" and word[0] not in {'%', '\\'}:
                    if word in map_word:
                        map_word[word] += 1
                    else:
                        map_word[word] = 1


print('\n'.join(
    f"{word}\t{score}"
    for word, score in sorted(map_word.items(), reverse=True, key=lambda x: x[1])
))

