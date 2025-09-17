from itertools import combinations
T = int(input())

def comb(cnt, idx):
    global answer
    if cnt == N//2:
        # 그룹 B = 전체 - A
        B = [i for i in range(N) if i not in A]

        # 그룹 A 시너지 계산
        A_sum = 0
        for x in A:
            for y in A:
                A_sum += arr[x][y]
                
                
        # 그룹 B 시너지 계산
        B_sum = 0
        for x in B:
            for y in B:
                B_sum += arr[x][y]

        # 최솟값 갱신
        answer = min(answer, abs(A_sum - B_sum))
        return
    
    for i in range(idx, N):
        A.append(i)
        comb(cnt+1, i+1)
        A.pop()
        



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e9
    # N//2개씩 2그룹나누기
    A = []
    comb(0, 0)
    print(f"#{tc} {answer}")