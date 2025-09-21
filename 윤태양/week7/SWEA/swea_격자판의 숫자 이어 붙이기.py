def dfs(count, idx, i, j):
    x,y = i,j
    if count == 7:
        if temp[:] not in pick:
            pick.append(temp[:])
        return
    
    for dx,dy in move:
        nx,ny = x+dx, y+dy
    



t = int(input())

for tc in range(t):
    graph = [list(map(int, input().split())) for _ in range(4)]
    move = [[-1,0],[1,0],[0,1],[0,-1]]
    pick = []
    temp = []