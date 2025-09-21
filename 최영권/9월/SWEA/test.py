def cal(x1,y1,x2,y2):
    s = abs(x1-x2)+abs(y1-y2)
    return s

def dfs(x,y,cnt,total):
    global answer

    # if total > answer:
    #     return

    if cnt == N:
        total+= cal(x,y,0,0)
        answer = min(answer, total)
        return

    for i in range(N):
        if not v[i]:
            v[i]=1
            nx,ny = lst[i]
            dfs (nx,ny,cnt+1,total+cal(x,y,nx,ny))
            v[i]=0
    
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    v = [0]*N
    answer = 99999999

    dfs (0,0,0,0)
    print(f"#{tc} { answer}")