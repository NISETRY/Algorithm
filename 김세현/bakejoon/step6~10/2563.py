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


print(result)
