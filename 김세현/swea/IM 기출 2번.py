# 3 # test case # 최대한 많은 인원으로
# 4 2 # 선수 들의 수 N, 실력 최대 차이 K
# 6 4 2 3 # -> 2,3,4 해서 정답은 3
# 4 3
# 1 2 3 4
# 4 1
# 1 3 7 5



# 풀이 1
# 투포인터? O(n^2)
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 나중에 대소비교해야해서 정수형으로 받음
    stats = list(map(int, input().split()))

    answer = 1 # 한명이라면 팀을 짤 필요가 없다? = 초기값을 0이라 할 필요 없다.

    # sorted(stats) 원본은 놔두고 정렬된 결과를 따로 // 하지만 이 문제에서는 졍렬된 값만 사용하면 된다. (메모리적으로)
    stats.sort()

    for i in range(N-1):
        temp = 1 # 초기값이 1인 이유: 한번 밀리면 팀원 2명
        for j in range(i+1, N):
            if stats[j] - stats[i] > K:
                break
            # else 를 안써도 된다. break가 있어서
            temp += 1
        answer = max(answer, temp)

    print(f'#{tc} {answer}')

# 풀이 2
# 슬라이딩 윈도우 O(n)
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 나중에 대소비교해야해서 정수형으로 받음
    stats = list(map(int, input().split()))

    answer = 1 # 한명이라면 팀을 짤 필요가 없다? = 초기값을 0이라 할 필요 없다.

    # sorted(stats) 원본은 놔두고 정렬된 결과를 따로 // 하지만 이 문제에서는 졍렬된 값만 사용하면 된다. (메모리적으로)
    stats.sort()

    left = 0
    right = 0

    while right < N:
        if stats[right] - stats[left] <= K:
            right += 1
            answer = max(answer, right-left+1)
            continue
        left += 1

    print(f'#{tc} {answer}')



# 회문 1
T = 10

for tc in range(1, T+1):
    N = int(input())

    graph = [input() for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(8-N+1):

            for k in range(N//2):
                if graph[i][j+k] != graph[i][j+N-1-k]:
                    break
            else:
                answer += 1

            for k in range(N//2):
                if graph[j+K][i] != graph[j+N-1-k][i]:
                    break
            else:
                answer += 1



# IM 문제
# 공이 상하좌우로 이동, 현재 칸보다 숫자가 작은 칸으로만 이동 가능. 가장 많이 이동할 수 있는 이동 횟수.
# 정리: 어디서 출발하면 가장 많이 이동할 수 잇는지 찾고, 그 최대 이동 수를 구하는 문재
# 이동할 때마다 이동 칸 수 plus 세기, 모든 칸에 대해 대해 시작해서 최대 이동 거리를 구한다.

"""
문제 복기:
NxN 크기의 격자판이 있다.
격자의 각 칸에는 정수가 하나씩 적혀 있다.
공은 어떤 칸에서 시작해서 상히좌우로 이동할 수 있다.
단, 이동할 수 있는 조건은 현재 칸보다 숫자가 작은 칸으로만 이동 가능하다.
이동할 때마다 공은 한 칸씩 이동하며, 이동할 수 있을 때까지 계속 이동한다.
가장 많이 이동할 수 있는 경우의 이동 횟수를 구하는 문제다. (정확히는, 출발칸을 포함한 "이동한 칸의 수"를 세는 것)
정리하면:
"어디서 출발하면 가장 많이 이동할 수 있는지 찾고, 그 최대 이동 수를 구하는 문제"
시작할 때i,j칸에서 출발해서,
매번 인접한 칸(상, 하, 좌, 우) 중 자기보다 작은 값이 있으면 그쪽으로 이동
이동을 반복하다가 더 이상 갈 곳이 없으면 이동을 멈춘다
출발할 수 있는 모든 칸을 다 시도해서, 그중 가장 많은 이동 수를 찾는 문제
"""

# T = int(input())
N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 시작점
for i in range(N):
    for j in range(N):
        

# def my_push(item):
#     s.append(item)


# size = 10
# stack = [0] * size
# top = -1
# # push(10, size)
# # top += 1
# # stack[top] = 20


# def my_pop():
#     global top
#     if top == -1:
#         print("underflow")
#         return 0 
#     else:
#         top -= 1
#         return stack[top+1]
    
# print(my_pop())


# stack = []
# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# top = -1
# stack = [0]*10

# top += 1       # push(1)
# stack[top] = 1
# top += 1      # push(2)
# stack[top] = 2
# top += 1       # push(3)
# stack[top] = 3

# top -= 1
# print(stack[top+1])
# top -= 1
# print(stack[top+1])
# top -= 1
# print(stack[top+1])

a1 = list(input().strip())
a2 = list(input().strip())

set_a1 = set(a1)
set_a2 = set(a2)

count = 0

for ch in a1:
    if ch in set_a2:
        count += 1

print(count)