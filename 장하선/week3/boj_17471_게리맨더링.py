# DFS
# 불능조건
# 1. 선거구가 3개 이상이 되는 경우
# 2. 선거구가 1개가 되는 경우
# 종합하면, 선거구는 반드시 2개여야만 한다
# 선거구 2개를 동시에 검증해야 함

# DFS로 선거구 이어가기
# 선거구 이어간 이후에는 남은 선거구가 이어지는지 확인
def dfs(gu):
    for i in nearby[gu]:
        linked_nearby.append[i]
        dfs(i)

from collections import deque

n=int(input())
# 인구수 input 받아주기
population=[0]+list(map(int, input().split()))
nearby=[[]for _ in range(n+1)]
nearby[0]=0
res=-1

for i in range(n): 
    tmp=list(map(int, input().split()))
    nearby[i+1]=tmp[1:]

for i in range(n):
    linked_nearby=[i]
    dfs(i)
ddd