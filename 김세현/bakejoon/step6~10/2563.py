N = int(input())
data = []
for i in range(N):
    num = list(map(int, input().split()))

    data.append(num)

y1 = int(data[2][1]+10)
y2 = int(data[0][1])

x1 = int(data[0][0] +10)
x2 = int(data[2][0])

print(y1)
result = 300 - (y1-y2)*(x1-x2)

print(result)
