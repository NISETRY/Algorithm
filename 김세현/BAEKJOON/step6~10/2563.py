<<<<<<< HEAD
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
=======
matrix = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())

for i in range(N):

    a, b = map(int, input().split())

    for i in range (10):
        for j in range(10):
            matrix[a+i][b+j] = 1


    result = 0
    for row in matrix:
        result += sum(row)

>>>>>>> a58587782f1f854fdb9f56d40272acf4eed5b266

print(result)
