matrix = []
for _ in range(9):
    num = list(map(int,input().split()))
    matrix.append(num)

max_num = max(map(max, matrix))

print (max_num)

for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_num:
            print(i+1, j+1)