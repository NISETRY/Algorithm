import pprint
grid = [[0]*100 for _ in range(100)]
sum = 0
for _ in range(4):
    sx, sy, ex,ey = map(int, input().split())
    
    for r in range(sx, ex):
        for c in range(sy, ey):
            grid[r][c] = 1
for row in range(100):
    for col in range(100):
        sum += grid[row][col]
print(sum)