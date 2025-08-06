Word = []


for _ in range(5):
    Word.append(list(input()))


for j in range(5):
    for i in range(4,-1,-1):
        print(Word[i][j], end='')



