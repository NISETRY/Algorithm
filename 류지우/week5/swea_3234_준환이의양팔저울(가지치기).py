# swea 3234번 준환이의 양팔 저울

# 1. 가지치기

import math # 팩토리얼 가져다 쓸거임

# 내가 무게 추를 고른 수 =count
def dfs(count, left, right):
    global answer

    if left >= total_weight/2 :
        answer += 2**(N-count)*math.factorial(N-count)
        return
    
    if count == N:
        answer += 1 # 경우의 수 한 번 발견 
        return 

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1 
        dfs(count+1,left+weights[i], right)

        if right+weights[i] <= left:
            dfs(count+1, left, right+weights[i])
        visited[i] = 0 # 원복

T = int(input())

for tc in range(1, T+1):
    answer = 0

    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)

    # 무게 추를 사용한 것인지 확인하기 위해서
    visited = [0]*N

    # dfs로 무게 추를 하나 골라서 넣는 방법임. 
    dfs(0, 0, 0) # 아무 것도 고르고, 안 놓은 상태에서 출발