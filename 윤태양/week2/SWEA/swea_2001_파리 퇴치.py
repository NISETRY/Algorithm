t = int(input())
  
for tc in range(t):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_kill = 0 
          
    for i in range(n-m+1):                  # 포문 인자로 영역 지정
        for j in range(n-m+1):
            kill = 0
            for x in range(m):
                for y in range(m):
                    kill += graph[i+x][j+y] # 킬 수 추가 
                      
            max_kill = max(max_kill, kill)
    print(f'#{tc+1} {max_kill}')