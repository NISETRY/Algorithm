t = int(input())

for tc in range(t):

    matrix = []
    for _ in range(9):
        c = list(map(int, input().split()))
        matrix.append(c)

    result = []

    for i in range(1, 8, 3):
        for j in range(1, 8, 3):

            a= (matrix[i][j], matrix[i-1][j], matrix[i+1][j],
                matrix[i][j+1], matrix[i-1][j+1], matrix[i+1][j+1],
                matrix[i][j-1], matrix[i-1][j-1], matrix[i+1][j-1] )
            
            if len(set(a)) == 9:
                result.append("CORRECT")
            else:
                result.append("INCORRECT")
                break

    

    for i in range(len(matrix)):
        if len(set(matrix[i])) == 9:
            result.append("CORRECT")
        else:
            result.append("INCORRECT")

 

    f= []

    for col in range(9):
        column = []
        for row in range(9):
            column.append(matrix[row][col])
        if len(set(column)) == 9:
            result.append("CORRECT")
        else:
            result.append("INCORRECT")
            break

    

    if "INCORRECT" in result:
        print( f'Case {tc+1}: INCORRECT')
    else:
        print( f'Case {tc+1}: CORRECT')