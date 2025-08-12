n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

    
for r in range(1, n+1):
    temp = list(map(int, input().split()))
    for c in range(1, temp[0]+1):
         graph[r].append(temp[c])

pick = []
temp = []
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

def bfs(a, group):
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
for i in pick:
    not_pick = list(set([1,2,3,4,5,6]) - set(i))
    if len(i)== 0 or len(not_pick) == 0:
        continue

    visited = [0]*(n+1)
    cnt1 = bfs(i[0], i)
    visited = [0]*(n+1)
    cnt2 = bfs(not_pick[0], not_pick)
    
    if cnt1+cnt2 !=n:
        continue
    
    area1 = 0
    area2 = 0
    for k in i:
        area1 += population[k]
    for k in not_pick:
        area2 += population[k]

    gap = min(gap, abs(area1 - area2))



if  gap == 999999999999999:
    print(-1)
else:
    print(gap)


# 선거구 조합 짜고 -> 연결되어 있는 지 확인 (sum(visited) == 6?)-> gap 확인
# 근데 not_picked 도 bfs 돌려야하는데 -> 그러면 not_picked를 만들어