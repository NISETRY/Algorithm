# 2738번
# r, c = map(int, input().split())
#
# matrix1 = [list(map(int, input().split())) for _ in range(r)]
# matrix2 = [list(map(int, input().split())) for _ in range(r)]
# matrix3 = [[0] * c for _ in range(r)]
# for i in range(r):
#     for j in range(c):
#         matrix3[i][j] += matrix1[i][j] + matrix2[i][j]
#         print(matrix3[i][j], end = ' ')
#     print()

# 2566번
mat = [list(map(int, input().split()) for _ in range(9))]
max_val = 0
r_idx = 0
c_idx = 0
for i in mat:
    if max(i) > max_val:
        max_val = max(i)
        r_idx = mat.index(i)
        c_idx = i.index(max_val)
print(max_val)
print(r_idx+1, c_idx+1)
# 10798번



# 2563번
