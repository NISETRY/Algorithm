# T = int(input())
 
# for tc in range(1, T+1):
#     a, b, c = map(int, input().split())
 
#     answer = 0
 
#     if b >= c:
#         answer += b - c + 1
#         b = c - 1
     
#     if a >= b:
#         answer += a - b + 1
#         a = b - 1
 
#     if a <= 0 or b <= 0:
#         answer = -1
 
#     print(f'#{tc} {answer}')


##############
# 1. 완전 탐색
# 2. 규칙 세우기

# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 3개 정도는 따로 받자
    A, B, C = map(int, input().split())

    # 불가능한 케이스를 먼저 지우자
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat_count = 0

    # B상자 = C상자 - 1 (B가 C보다 크거나 같을 때만)
    if B >= C:
        eat_count += B - (C-1)
        B = C - 1

    # A상자 = B상자 - 1 (A가 B보다 크거나 같을 때만)
    eat_count += A - (B-1)
    A = B - 1

    print(f'#{tc} {eat_count}')