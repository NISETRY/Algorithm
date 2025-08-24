import pprint

N = int(input())
key = int(input())
x,y = N//2, N//2
grid = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0

grid[x][y] = 1
num = 1


time = []
for t in range(1, N):
    time.append(t)
    time.append(t)
    if t == N-1:
        time.append(t)

for t in time:
    for _ in range(t):
        x += dr[d]
        y += dc[d]
        num += 1
        grid[x][y] = num
    d = (d+1)%4


for r in range(1, N+1):
    for c in range(1, N+1):
        print(grid[r-1][c-1], end =' ')
    print()

for r in range(1, N+1):
    for c in range(1, N+1):
        if grid[r-1][c-1] == key:
            print(r, c)