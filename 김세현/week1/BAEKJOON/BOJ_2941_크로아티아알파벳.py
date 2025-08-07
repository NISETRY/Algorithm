word = input()

croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for ch in croatian:
    word = word.replace(ch, '*')

print(len(word))