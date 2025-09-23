# 3개의 상자 
# A개 사탕상자 
# B개 사탕상자
# C개 사탕상자
# 모든 상자가 비면 안댐
# A < B < C 

# 몇개의 사탕을 먹어야하나

T = int(input())

for tc in range(1, T+1):
    A, B, C = list(map(int, input().split()))
    answer = 0 
    if B >= C:
        answer += B - (C-1)
        B = C - 1

    if A >= B:
        answer += A - (B-1)
        A = B - 1
    if A <= 0 or B <= 0 or C <= 0:
        answer = -1
    print(f"#{tc} {answer}")