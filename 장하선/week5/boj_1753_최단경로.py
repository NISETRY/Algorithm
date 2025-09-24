from heapq import heappop, heappush
import sys
input=sys.stdin.readline

def dijkstra(start):
    
    pq=[]
    # 시작점은 0으로 해서 pq에 담아줌
    heappush(pq, (0,start))
    # 거리값도 0으로 바꾸기
    distance[start]=0
    
    while pq:
        # 거리와 현재 노드를 pq에서 pop함
        dist, cur = heappop(pq)
        # 최솟값 미발견시 continue
        if distance[cur]<dist:
            continue
        # 최솟값 발견 시
        for i in roots[cur]:
            if dist+i[1]<distance[i[0]]:
                distance[i[0]]=dist+i[1]
                heappush(pq, (dist+i[1],i[0]))

V,E=map(int,input().split())
# 시작 정점의 번호
k=int(input())
roots=[[] for _ in range(V+1)]
visited=[0]*E
# 일단 모든 간선의 거리를 최댓값으로
distance=[float('inf')]*(V+1)
# 입력 받기
for i in range(E):
    # u->v로 가는 가중치 w의 간선 존재, u<->v가 아님에 주의할 것
    u,v,w=map(int,input().split())
    # u번에서 갈 수 있는 노드와 가중치를 append
    roots[u].append((v,w))

dijkstra(k)

# 출력 형식
for i in range(1,V+1):
    print(distance[i] if distance[i]<float('inf') else 'INF')