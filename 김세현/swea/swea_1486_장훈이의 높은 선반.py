N, B = map(int, input().split())
heights = list(map(int, input().split()))

picked = []

# 조합
def comb(count, idx):
    s = sum(picked)

    print(picked)

    if count == N:
        return
    
    for i in range(idx, len(heights)):
        picked.append(heights[i])
        comb(count + 1, i + 1)
        picked.pop()

comb(0, 0)
        
# import sys
# sys.stdin = open("input.txt")


# 종료조건: N명의 모든 점원을 고려했을 때
# - 가지치기: 이미 높이가 B이상이면 더 이상 쌓을 필요 없다
# 가지의 수:
# - 점원을 탑에 포함 시키는 경우 or 안시키는 이유
# 부분집합 문제, 정확한 개수를 말하지 않아서
def recur(idx, total_height):
    if total_height >= B: # 가지치기: B이상이면 더 이상 X
        min_answer = min(min_answer, total_height)
        return
    
    if idx == N:
        return 
    
    recur(idx + 1, total_height + heights[idx]) # 탑에 포함 시키는 경우
    recur(idx + 1, total_height) # 탑에 포함 안 시키는 경우

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_answer = 1e9 # 나올 수 있는 최대 범위 
    # min_answer = 10000 * N
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')
