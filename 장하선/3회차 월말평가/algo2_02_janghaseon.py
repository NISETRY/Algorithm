import sys
sys.stdin=open('input.txt')

T=int(input())

def dfs(x):
    global tmp
    if 0 not in visited:
        return
    cand=[]
    for i in range(V+1):
        if graph[x][i]!=0 and not visited[i]:
            cand.append((i,graph[x][i]))
    # 전체 후보자 중 가장 최단거리로 이동하기 위한 로직
    if cand:
        temp=cand[0]
        for i in cand:
            if temp[1]>i[1]:
                temp=i
        tmp+=temp[1]
        visited[temp[0]]=1
        dfs(temp[0])
    # cand가 비었다면 모든 노드 연결이 안 되었는데 더 이상 못 가는 노드라는 것
    else:
        tmp=999999999
        return

for tc in range(1,T+1):
    V,E=map(int,input().split())
    # 인접 리스트로 저장
    graph=[[0]*(V+1) for _ in range(V+1)]
    res=0
    for i in range(E):
        u,v,w=map(int,input().split())
        graph[u][v]=graph[v][u]=w
        res+=w
    # 시작을 모든 노드(0~V)에서 진행
    for i in range(V+1):
        tmp=0
        visited=[0]*(V+1)
        visited[i]=1
        dfs(i)
        res=min(res,tmp)
    print(f'#{tc} {res}')

