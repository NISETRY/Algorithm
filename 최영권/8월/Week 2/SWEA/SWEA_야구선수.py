# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())

#     player = list(map(int, input().split()))
#     max_team = 0
#     sort_player = sorted(player)

#     # 
#     for i in range(len(sort_player)-1, -1, -1):
        
#         for j in range()
            
        
    
#     print(f"#{tc} {length}")

    
# 정렬을 해서 2중 for문 -> 최악의 경우 시간복잡도 N^2
# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())  # N: 선수들의 수, K:선수들의 실력차이

#     stats = list(map(int, input().split()))
    
#     answer = 1

#     # 두 명이상 팀이 될까?
#     # 원본을 사용할 일 없으니까 sorted보다 sort가 효율적
#     stats.sort()

#     for i in range(N-1):
#         # 기준점마다 몇 칸 가는지 기록
#         temp = 1
#         for j in range(i+1, N):
#             if stats[j] - stats[i] > K:
#                 break
#             temp += 1    

#         answer = max(answer, temp)
#     print(f"#{tc} {answer}")
            


# Two 포인터 -> 
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 선수들의 수, K:선수들의 실력차이

    stats = list(map(int, input().split()))

    answer = 1
    stats.sort()

    left = 0
    right = 0

    while right < N:
        if stats[right] - stats[left] <= K:
            right += 1
            answer = max(answer, right-left)
            continue
        left += 1
        
    print(answer)