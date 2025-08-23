k = int(input())
m, n= map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
graph[n-1][m-1] = 2
move1 = [[-1,0],[0,-1],[0,1],[1,0]]
move2 = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]


def bfs(a,b):
    answer = 0
    visited[a][b] = 1
    que = [[a,b,0]]
    
    while que:
        answer += 1
        for _ in range(len(que)):
            x, y, jump = que.pop(0)
            if graph[x][y] == 2:
                return answer
            
            if jump < k:
                for dx,dy in move2:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m:
                        if visited[nx][ny] < jump  and graph[nx][ny] != 1:
                            visited[nx][ny] = jump+1
                            que.append((nx,ny,jump+1))
                            
            for dx,dy in move1:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] < jump and graph[nx][ny] != 1:
                        visited[nx][ny] = jump
                        que.append((nx,ny,jump))
            
    return -1
    
ans = bfs(0,0)

if ans == -1:
    print(ans)
else:
    print(ans-1)

print(graph)