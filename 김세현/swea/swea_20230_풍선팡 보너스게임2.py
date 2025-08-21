# T = int(input())

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

sum_garo = 0
sum_saro = 0
sum = 0
max_sum = 0

# 시작점
for i in range(N):
    sum_garo = sum(arr[i])
    for j in range(N):   
        sum_saro = sum(arr[j][i])
        
        sum = sum_garo[i] + sum_saro[j] - arr[i][j]

        if max_sum < sum:
            max_sum = sum
            
print(max_sum)
