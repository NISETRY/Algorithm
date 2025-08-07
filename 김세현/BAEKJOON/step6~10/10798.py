<<<<<<< HEAD
Word = []


for _ in range(5):
    Word.append(list(input()))


for j in range(5):
    for i in range(4,-1,-1):
        print(Word[i][j], end='')



=======
words = []
length = []
for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

result = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += words[j][i]

print(result)
>>>>>>> a58587782f1f854fdb9f56d40272acf4eed5b266
