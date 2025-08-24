N = int(input()) # 크기 입력
where = int(input())

result = [[0]*N for _ in range(N)] # 크기만큼 0으로 배열

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 첫 시작은 정 가운데
x = y = N // 2
num = 1
result[x][y] = num
num += 1
step = 1 # 한칸씩 이동

while num <= N*N:
    for move in range(4):
        for _ in range(step):
            if num > N*N:
                break # 벗어나면 멈춤

            x += di[move]
            y += dj[move]
            result[x][y] = num
            num += 1

            # 1 1 2 2 3 3 4 4 5 5 ..
            # step을 조정해야 함
            # 홀수.. 일 때 +1 ?
        if move % 2 == 1:
            step += 1

# 찾고자 하는 숫자의 위치
where_x, where_y = 0, 0
for i in range(N):
    for j in range(N):
        if result[i][j] == where:
            where_x = i+1
            where_y = j+1

for row in result:
    print(*row)

print(where_x, where_y)

        
    

