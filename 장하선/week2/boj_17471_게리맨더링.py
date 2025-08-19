# 선거구를 나눌 수 있는 모든 경우의 수 확인
# 위에서 구한 case 별 인구차를 list에 저장
# 
from collections import deque
n=int(input())
population=list(map(int,input().split()))
nearby=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    near=list(map(int,input().split()))
    for j in range(1,len(near)):
        nearby[i+1][near[j]]=nearby[near[j]][i+1]=1
queue=deque([1])
def dfs():
