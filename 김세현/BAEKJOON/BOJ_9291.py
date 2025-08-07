matrix = []
for _ in range(9):
    c = list(map(int, input().split()))
    matrix.append(c)

# for i in range(1, 8, 3):
#     for j in range(1, 8, 3):

#         a= (matrix[i][j], matrix[i-1][j], matrix[i+1][j],
#             matrix[i][j+1], matrix[i-1][j+1], matrix[i][j+1],
#             matrix[i][j-1], matrix[i-1][j-1], matrix[i+1][j-1] )
        
#     if set(a) == a:
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#         break

# m = [1, 2, 3, 5, 6, 7, 4, 8, 9]

# if m == list(set(m)):
#     print("CORRECT")
# else:
#     print("INCORRECT")



# if len(set(m)) == 9:
#     print("CORRECT")
# else: 
#     print("INCORRECT")
# 1. 매 줄마다 set
# 2. 

f= []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        f.append(matrix[i][j])

d = []
for i in range(0, len(f), 9):
    chunk = f[i:i+9]
    d.append(set(chunk))

    if len(set(d)) == 9:
        print("CORRECT")
    else:
        print("INCORRECT")
        break