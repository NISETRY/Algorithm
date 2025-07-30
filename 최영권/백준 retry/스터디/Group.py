# SWEA View


for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        if max(buildings[i-2:i+3]) == buildings[i]:
            answer += buildings[i] - sorted(buildings[i-2:i+3])[-2]
    print(f"#{tc} {answer}")