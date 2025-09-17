T = int(input())


# 종료조건 : 모든 숫자를 고려
# 시작점 : 1개의 숫자부터 시작
# 누적값 : 몇 개 숫자 고려했는지, 계산된 결과, 남은 연산자 수
# 가지의 수 : 4가지(연산자가 없으면 못쓴다)
def recur(cnt, total, plus, minus, multi, div):
    global min_result, max_result
    if cnt == N:
        # Todo: 최대, 최소계산
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    # 덧셈
    if plus > 0:
        recur(cnt + 1, total + numbers[cnt], plus - 1, minus, multi, div)
    # 뺄셈
    if minus > 0:
        recur(cnt + 1, total - numbers[cnt], plus , minus - 1, multi, div)
    # 곱셈
    if multi > 0 :
        recur(cnt + 1, total * numbers[cnt], plus , minus, multi - 1, div)
    # 나눗셈
    if div > 0:
        recur(cnt + 1, int(total / numbers[cnt]), plus , minus, multi, div - 1)


for tc in range(1, T+1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    min_result = 1e9
    max_result = -1e9
    
    recur(1, numbers[0], *opers)
    print(f"#{tc} {max_result-min_result}")