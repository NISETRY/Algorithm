# for tc in range(10):

#     N = 8
#     num = int(input())

#     arr = [list(input().strip()) for _ in range(N)]

#     count = 0

#     # 가로 방향 회문 찾기
#     for i in range(N):
#         for j in range(N - num + 1): 
#             word = arr[i][j:j+num]
#             if word == word[::-1]:
#                 count += 1

#     # 세로 방향 회문 찾기
#     for i in range(N - num + 1):
#         for j in range(N):
#             word = ""
#             for k in range(num):
#                 word += arr[i+k][j]
#             if word == word[::-1]:
#                 count += 1

#     print(f'#{tc+1} {count}')

N = int(input())

arr = [list(input().strip()) for _ in range(8)]

cnt = 0

# 가로 검사
for i in range(8):
    for j in range(8-N+1):
        for k in range(N//2):
            if arr[i][j+k] != arr[i][j+N-k-1]:
                break
        else:
            cnt += 1

# 세로 검사
        for k in range(N//2):
            if arr[j+k][i] != arr[j+N-1-k][i]:
                break
        else:
            cnt += 1

print(cnt)