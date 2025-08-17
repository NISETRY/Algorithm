n = int(input())
target = int(input())

graph = [[0]*n for _ in range(n)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

x = y = n // 2   # 센터 고정
graph[x][y] = 1  # 가운데는 1박고 시작
step = 1         # 스텝
num = 2          # 첫 넣을 숫자
tx, ty = (x, y) if target == 1 else (-1, -1)

while num <= n*n:
    for m in range(4):
        dx, dy = move[m]

        for _ in range(step):  # 반복 횟수가 그래프의 레인지를 넘을 수 있기 때문에 break
            if num > n*n:
                break

            x += dx
            y += dy
            graph[x][y] = num
            
            if num == target:
                tx, ty = x, y
            num += 1

        if m % 2 == 1:  # 스텝은 1 2 2 3 3 ... 홀수일 때 증가함
            step += 1

for row in graph:
    print(*row)
print(tx+1, ty+1)

