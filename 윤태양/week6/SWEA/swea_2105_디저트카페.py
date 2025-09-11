def dfs(count, x, y, dp, desert_count,sx,sy):
    global answer 

    if count == 3 and x == sx and y == sy:
        answer = max(desert_count, answer)
        return
    
    if count >= 4:
        return
 
    dx,dy = move[count] # 직진
    nx,ny = dx+x, dy+y
    if 0<=nx<n and 0<=ny<n:
        if not (dp & (1 << graph[nx][ny])):
            new_dp = dp | (1 << graph[nx][ny]) 
            dfs(count,nx,ny,new_dp,desert_count+1,sx,sy)

    if count < 3:
        dx,dy = move[count+1] # 좌회전
        nx,ny = dx+x, dy+y
        if 0<=nx<n and 0<=ny<n:
            if not (dp & (1 << graph[nx][ny])):
                new_dp = dp | (1 << graph[nx][ny])
                dfs(count+1,nx,ny,new_dp,desert_count+1,sx,sy)


t = int(input())

for tc in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    move = [(1,-1),(1,1),(-1,1),(-1,-1)] # 좌하향, 우하향, 우상향, 좌상향
    answer = -1

    for i in range(n):
        for j in range(n):
            dp = 0
            dfs(0,i,j,dp,0,i,j)

    print(f'#{tc+1} {answer}')





# 디저트 카페 순회하는 거 -> dfs
# 가지치기 -> memorization / set / 안에 번호 있으면 종료 / 좌회전 4번 이상하면 종료
# 종료조건: 처음으로 돌아오면 종료
# visited는 해보면서 하자 / 아마도 돌 때마다 visited 초기화 하거나 아니면 어차피 두 방향밖에 못가기 때문에 상관 x 일텐데..