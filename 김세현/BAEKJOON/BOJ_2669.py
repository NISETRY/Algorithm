# 빈 영역 만들고 해당 하는 만큼 1 입력하고, 넓이가 2이상인 것들의 개수?

# 빈 영역
arr = [[0] * 100 for _ in range(100)]

# 꼭짓점 입력 받기
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] += 1

count = 0

for x in range(100):
    for y in range(100):
        if arr[x][y] >= 1:
            count += 1
print(count)


