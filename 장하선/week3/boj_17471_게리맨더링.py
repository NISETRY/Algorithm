# DFS
# 불능조건
# 1. 선거구가 3개 이상이 되는 경우
# 2. 선거구가 1개가 되는 경우
# 종합하면, 선거구는 반드시 2개여야만 한다
# 선거구 2개를 동시에 검증해야 함
import pprint
from collections import deque

n=int(input())
# 인구수 input 받아주기
population=list(map(int, input().split()))
total_population=sum(population)
# 인접 list로 선거구 별 근접지점 확인
nearby=[[]for _ in range(n+1)]
# idx 맞춰주고, 앞의 0번 선거구는 없으니까 0으로 처리
nearby[0]=[0]
for i in range(n):
    tmp=list(map(int, input().split()))
    nearby[i+1]=tmp[1:]

def blue_red(team):
    if not team:
        return False
    elif len(team)==1:
        return True
    
    queue=deque([team[0]])
    visited=[False for _ in range(n+1)]
    visited[team[0]]=True
    cnt=1

    while queue:
        x=queue.popleft()
        for i in nearby[x]:
            if i in team and not visited[i]:
                visited[i]=True
                queue.append(i)
                cnt+=1
    return cnt==len(team)

for idx in range(1,n+1):
    blue_red(idx)