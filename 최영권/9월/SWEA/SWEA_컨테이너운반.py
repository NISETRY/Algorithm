# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split()) 
#     boxes = list(map(int, input().split()))
#     trucks = list(map(int, input().split()))
#     answer = 0
    
#     boxes.sort(reverse=True)
#     trucks.sort(reverse=True)
#     box_idx = 0
#     truck_idx = 0

#     while box_idx < N and truck_idx < M:
#         if boxes[box_idx] <= trucks[truck_idx]:
#             answer += boxes[box_idx]
#             box_idx += 1
#             truck_idx += 1
#         else:
#             box_idx += 1
#     print(f"#{tc} {answer}")
    
from itertools import combinations
print(combinations([1,2,3,4,5], 3))

for case in combinations([1,2,3,4,5], 3):
    print(case)