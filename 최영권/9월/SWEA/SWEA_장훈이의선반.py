T = int(input())
picked = []
def comb(cnt, idx):
    global answer
    
    if sum(picked) >= B:
        answer = min(answer, sum(picked) - B)  

    if cnt == len(heights):
        return
    for i in range(idx, len(heights)):
        picked.append(heights[i])
        comb(cnt+1, i+1)
        picked.pop()


for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = 1e10
    comb(0,0)
    print(f"#{tc} {answer}")