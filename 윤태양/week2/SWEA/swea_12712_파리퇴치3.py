t = int(input())
 
for tc in range(t):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]  # 인풋 받기
 
    move1 = [[-1,0],[1,0],[0,1],[0,-1]]                          # + 델타
    move2 = [[1,1],[1,-1],[-1,1],[-1,-1]]                        # x 델타
    max_kill = 0
 
    for i in range(n):
        for j in range(n):
             
            kill = 0
            for k in move1:
                for l in range(m):
                    if 0<=i+k[0]*l<n and 0<=j+k[1]*l<n:          # + 파리퇴치 수 계산
                        kill += graph[i+k[0]*l][j+k[1]*l]
                         
            max_kill = max(kill-graph[i][j]*3, max_kill)         # 처음 자리가 4번 계산되었기 때문에 3번 빼줌
 
            kill = 0
            for k in move2:
                for l in range(m):
                    if 0<=i+k[0]*l<n and 0<=j+k[1]*l<n: 
                        kill += graph[i+k[0]*l][j+k[1]*l]         # x 파리 퇴치 수 계산
 
            max_kill = max(kill-graph[i][j]*3, max_kill)
 
    print(f'#{tc+1} {max_kill}')