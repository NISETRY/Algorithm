# kruscal -> 가중치 기준으로 간선들을 "정렬"
# 사이클 발생 시 선택 X, 서로소 집합
import sys
# import heapq
from heapq import heappush, heappop
sys.stdin = open("C:/Users/SSAFY/Desktop/Algorithm/최영권/9월/SWEA/input.txt", "r")



def find_set(x):
    if x == parents[x]:
        return x
    
    # 기본코드
    # return find_set(parents[x])
    
    # 경로 압축
    # 결국 대표자가 return
    parents[x] = find_set(parents[x])
    return parents[x]    
    
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return
    
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry   



V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

# 가중치 기준 오름차순 정렬
edges.sort(key = lambda x:x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택
# - 사이클이 발생하면 고르지 말자!
# - 언제까지?
# -   MST가 완성될때까지
# -   == V-1개를 선택할 때 까지
cnt = 0    # 현재 선택한 간선의 수
result = 0 # 가중치의 합

parents = [i for i in range(V)] # make_set



for u, v, w in edges:
    # 사이클이 아니라면
    # - 연결 ( 같은 집합으로 만든다 )
    # - cnt + 1
    # - cnt가 V-1이면 종료
    if find_set(u) != find_set(v): # -> 사이클검증 함수 1개 : 서로소 집합 사용
        union(u, v)
        cnt += 1
        result += w
        
        if cnt ==V-1:
            break
print(result)