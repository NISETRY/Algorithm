T=int(input())
for t in range(1, T+1):
    n=int(input())
    snail=[[0 for _ in range(n)] for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    def snail_dance(x,y,dir,num):
        snail[x][y]=num
        nx, ny = x+dx[dir], y+dy[dir]
        if num==n**2: # 탈출조건
            return
        if (0<=nx<n and 0<=ny<n) and snail[nx][ny]==0:
            snail_dance(nx,ny,dir,num+1)
        else:
            dir=(dir+1)%4
            snail_dance(x,y,dir,num)
    snail_dance(0,0,0,1)
    print(f'#{t}')
    for i in range(n):
        print(*snail[i])