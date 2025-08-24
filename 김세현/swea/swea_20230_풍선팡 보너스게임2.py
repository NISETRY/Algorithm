<<<<<<< HEAD
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
=======
T = int(input())

for tc in range(T):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # 가로줄, 세로줄 저장해놓기

    sum_garo = [0] * N
    sum_sero = [0] * N

    for i in range(N):
        for j in range(N): 
            sum_garo[i] += arr[i][j]
            sum_sero[i] += arr[j][i]
        

    for i in range(N):
        sum_i = 0
        for j in range(N):
            sum_i = sum_garo[i] + sum_sero[j] - arr[i][j]

            if sum_i > max_sum:
                max_sum = sum_i
            print(sum_i)

    print(f'#{tc+1} {max_sum}')

>>>>>>> a29b2439cdd3ff779b66fe5c6a4f02e7936ecbc1
