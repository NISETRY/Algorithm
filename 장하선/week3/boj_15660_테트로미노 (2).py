# 1과 차이점
# 1. 2개를 놓는다
# 2. 놓은거 위에 놓을수도 있고, 아닐수도 있는데
# 3. 위에 놓는지 visited로 이를 점검

import heapq

# 끔찍한 shapes 먼저 만들어주기
shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],# 0
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],# 2
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],# 4
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],# 6
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],# 8
    [(1, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],# 10
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],# 12
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],# 14
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],# 16
    [(0, 1), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)] # 18
]

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
res=0

def tetro(i,j):
    global res
    res1,res2=0,0
    for shape in shapes:
        visited=[[0 for _ in range(m)] for _ in range(n)]
        tmp=0
        quatro=0
        for x,y in shape:
            nx,ny=i+x,j+y
            if 0<=nx<n and 0<=ny<m:
                tmp+=board[nx][ny]
                visited[nx][ny]=1
                quatro+=1
            else:
                break
        res1=max(res1,tmp)
        # 1차 테트로미노 확인 끝
        if quatro==4:
            for a in range(n):
                for b in range(m):
                    for shape1 in shapes:
                        tmp1=0
                        for x,y in shape1:
                            mx,my=a+x,b+y
                            if 0<=mx<n and 0<=my<m and visited[mx][my]==0:
                                tmp1+=board[mx][my]
                            else:
                                break
                        res2=max(res2,tmp1)
    res=max(res, res1+res2)
    return res

for i in range(n):
    for j in range(m):
        tetro(i,j)
print(res)