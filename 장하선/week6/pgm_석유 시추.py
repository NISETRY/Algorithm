# TLE code
# 전체 BFS를 계속 도니까 case가 큰 경우에는 TLE 발생
from collections import deque
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def solution(land):
    n,m=len(land), len(land[0])
    ans=0
    for i in range(m):
        queue=deque([])
        visited=[[0 for _ in range(m)] for _ in range(n)]
        tmp=0
        for j in range(n):
            # queue에 1 만나면 일단 저장하고, 1 있는 거를 싹 다 돌려버림
            if land[j][i]==1:
                queue.append((j,i))
                visited[j][i]=1
                tmp+=1
        # BFS
        while queue:
            r,c=queue.popleft()
            for d in range(4):
                nr,nc=r+dr[d],c+dc[d]
                if not (0<=nr<n and 0<=nc<m):
                    continue
                if land[nr][nc]==1 and not visited[nr][nc]:
                    queue.append((nr,nc))
                    visited[nr][nc]=1
                    tmp+=1
        # 답 최댓값 갱신
        ans=max(ans, tmp)
    return ans

# TLE 해결을 위한 방법
# 일단 전체 땅을 먼저 한 번만 스캔하면서
# 스캔하는 중 1 발견하면 BFS 시작
# 석유 한 덩어리를 모두 스캔하면 
# 그 덩어리가 있던 행에 덩어리의 크기를 모두 입력하는 oil 변수 선언
from collections import deque
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def solution(land):
    n,m=len(land), len(land[0])
    visited=[[0 for _ in range(m)] for _ in range(n)]
    oil=[[] for _ in range(m)]
    ans=0
    queue=deque([])
    for i in range(m):
        for j in range(n):
            # 석유 발견
            if land[j][i]==1 and not visited[j][i]:
                queue.append((j,i))
                visited[j][i]=1
                tmp=1
                # set 자료형을 사용해서 중복 방지
                oil_row={i}
                while queue:
                    r,c=queue.popleft()
                    for d in range(4):
                        nr,nc=r+dr[d],c+dc[d]
                        if not (0<=nr<n and 0<=nc<m):
                            continue
                        if land[nr][nc]==1 and not visited[nr][nc]:
                            queue.append((nr,nc))
                            visited[nr][nc]=1
                            tmp+=1
                            oil_row.add(nc)
                # 석유 한 덩어리를 확인 완료하면 oil_row 안에 있는 행 정보를 확인하고
                # 그 행들에 덩어리 크기 입력
                for x in oil_row:
                    oil[x].append(tmp)
    # 답 갱신하는 로직
    for i in range(m):
        tmp=0
        for num in oil[i]:
            tmp+=num
        ans=max(ans,tmp)
    return ans
