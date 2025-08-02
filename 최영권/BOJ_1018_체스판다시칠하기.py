import pprint

 
N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
miss = 0

# W, B 세팅
event = ['W', 'B']
first_chr = chess[0][0]
del event[event.index(first_chr)]
second_chr = event[0]
print(first_chr, second_chr)


# 정답판 생성
correct_chess = [[first_chr] * M for _ in range(N)]
 
for i in range(len(correct_chess)):
    for j in range(len(correct_chess[i])):
        if i % 2 == 0:
            if j % 2 == 1:
                correct_chess[i][j] = correct_chess[i][j].replace(first_chr, second_chr)
            else:
                continue

        else:
            if j % 2 == 0:
                correct_chess[i][j] = correct_chess[i][j].replace(first_chr, second_chr)
            else:
                continue


# 비교
