import sys
sys.stdin=open('input.txt')

#1 2
#2 2
#3 8
#4 57
#5 151
#6 257
#7 18
#8 160
#9 414
#10 395

from heapq import heappop,heappush
# 상하좌우
dr=[-1,1,0,0]
dc=[0,0,-1,1]

def dijkstra():
    # 도달한 적 없는 지점을 임의의 최댓값으로 설정
    distance=[[9e6 for _ in range(n)] for _ in range(n)]
    # 출발점은 0으로부터 시작하니 0으로 갱신
    distance[0][0]=0
    # pq : cost(비용), 위치
    pq=[(0,0,0)]
    # BFS
    while pq:
        # heapq의 정렬은 맨 앞의 원소를 기준으로 하기 때문에 cost를 맨 앞에 넣어줌.
        cost,r,c=heappop(pq)
        # 사방 탐색
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            # 경계 벗어나면 skip
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            # 임시 cost 설정하고 최솟값인지 확인
            cost_tmp=cost+road[nr][nc]
            # 최솟값이 아니면 skip
            if cost_tmp>=distance[nr][nc]:
                continue
            # 최솟값이라면 최솟값 갱신 후 pq에 heappush
            distance[nr][nc]=cost_tmp
            heappush(pq,(cost_tmp,nr,nc))
    # 최종 결과물 : 도착점에서의 최소 비용
    return distance[n-1][n-1]

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    road=[list(map(int,input().strip())) for _ in range(n)]
    ans=dijkstra()
    print(f'#{tc} {ans}')