# 문제 설명
# 인구수가 적혀있는 n개의 선거구가 주어지고, 각 선거구 마다 간선이 주어진다.
# 그 때 간선으로 연결된 두 선거구의 조합 중 가장 인구수가 덜 차이나도록 구해라.
# 만약 두 선거구로 묶을 수 없으면 -1 출력 

n = int(input())                        
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]  # 인풋

    
for r in range(1, n+1):
    temp = list(map(int, input().split()))
    for c in range(1, temp[0]+1):
         graph[r].append(temp[c])  # 간선 연결 / 양 방향을 모두 주기 때문에 한 번만 해줘도 된다.

pick = []
temp = []                         # 선거구 조합 
def comb(count, idx):
     pick.append(temp[:])
     if count == n:
          return
     
     for i in range(1, n+1):
          if i> idx:
            temp.append(i)
            comb(count+1, i)
            temp.pop()

comb(0,0)

def bfs(a, group):               # 선거구 연결 확인용 bfs
    visited[a] = 1
    que = [a]
    cnt = 1

    while que:
        x = que.pop(0)
        for i in graph[x]:
            nx = i
            if visited[nx] == 0 and nx in group:
                que.append(nx)
                visited[nx] = 1
                cnt+=1
  
    return cnt
gap = 999999999999999
for i in pick: # pick = 조합으로 선택된 선거구
    not_pick = list(set(o for o in range(1, n+1)) - set(i))  # not_pick = 전체 - 선거구 -> 여집합
    if len(i)== 0 or len(not_pick) == 0:
        continue

    visited = [0]*(n+1)   # pick 선거구의 첫번째 요소 bfs
    cnt1 = bfs(i[0], i)
    visited = [0]*(n+1)   # not_picked 선거구 첫번째 요소 bfs
    cnt2 = bfs(not_pick[0], not_pick) 
    
    if cnt1+cnt2 !=n:     # 첫번째 요소 선거구 bfs를 더한 값이 n이 아니면,
        continue          # 모든 선거구가 연결이 안된 것 -> continue 
        
    
    area1 = 0
    area2 = 0
    for k in i:
        area1 += population[k]  # 선거구별로 인구수 값 구하기
    for k in not_pick:
        area2 += population[k]

    gap = min(gap, abs(area1 - area2)) # 갱신



if  gap == 999999999999999:   # 모든 경우의수가 연결 x -> print(-1)
    print(-1)
else:
    print(gap)               # 아니면 min gap 출력
