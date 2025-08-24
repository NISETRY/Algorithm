N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]

# 가로 확인하기
result = ''
for i in range(N):
    for j in range(N-M+1):
        word = ''.join(arr[i][j:j+M])
        if word == word[::-1]:
            result = word

# 세로 확인하기
for j in range(N):
    for i in range(N-M+1):
        word = ''.join(arr[i:i+M][j])
        if word == word[::-1]:
            result = word

print(result)
