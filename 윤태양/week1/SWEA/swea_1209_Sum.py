for tc in range(10):
    input()
    graph = [[0]*100 for _ in range(100)]
    for r in range(100):
        l = list(map(int, input().split()))
        for c in range(100):
            graph[r][c] = l[c]
    max_r, max_c, max_rc, max_cr = 0,0,0,0 ## 인풋, 초기세팅
  
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += graph[i][j]
        max_r = max(max_r, temp)
  
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += graph[j][i]
        max_c = max(max_c, temp)
  
    temp_rc = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                temp_rc += graph[i][j]
    max_rc = max(max_rc, temp_rc)
          
    temp_cr = 0
    for i in range(100):
        for j in range(100):
            if 99-i == j:
                temp_cr += graph[100-i-1][j]
    max_cr = max(max_cr, temp_cr)
  
    print(f'#{tc+1} {max(max_c,max_r,max_cr,max_rc)}')