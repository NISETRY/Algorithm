import pprint

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
# pprint.pprint(chess)

def make_correct(chess):

    # W, B 세팅
    event = ['W', 'B']
    for chr in event:

        first_chr = chr
        del event[event.index(first_chr)]
        second_chr = event[0]


        # 정답판 생성
        correct_chess = [[first_chr] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
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
    return correct_chess
print(make_correct('W'))

# 비교
# minimum = 8*8

# for row in range(N - 7):
#     for col in range(M - 7):
#         cnt = 0
#         cur_chess = [line[col:col+8] for line in chess[row:row+8]]
#         correct_chess = make_correct(cur_chess[0][0])
#         # pprint.pprint(cur_chess)
#         # print('===============================================================')
#         # pprint.pprint(correct_chess)
#         # print('===============================================================')
#         for i in range(8):
#             for j in range(8):
#                 if cur_chess[i][j] != correct_chess[i][j]:
#                     cnt += 1
        
#             if cnt < 32:
#                 pass
#             elif 32 < cnt <= 64:
#                 cnt = 64 - cnt
#         if cnt < minimum:
#             minimum = cnt
# print(minimum)