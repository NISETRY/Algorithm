import pprint

T = int(input())
t = [list(map(int, input().split())) for _ in range(T)]

# 최대값 구해서 영역만들기
max_size = []
for line in zip(*t):
    max_size.append(max(list(line)))
grid = [[0]*(max_size[0]+11) for _ in range(max_size[-1]+11)] # 0~25 : 26개, 0~17까지 : 18개

# 1찍기
for xy in t:
    x = xy[0]
    y = xy[-1]+1  # 넓이 구할때는 테두리 전부 1찍으면 11*11 사이즈 -> 한 쪽 조정
    # print(x, y) 
    # # print("===============output=============")
    for i in range(10):
        for j in range(10):
            grid[y+j][x+i] = 1
# print(len(grid), len(grid[0]))
# pprint.pprint(grid)
total = 0
# total = sum(map(sum, grid))...
for r in grid:
    for c in r:
        sum += c
print(total) 