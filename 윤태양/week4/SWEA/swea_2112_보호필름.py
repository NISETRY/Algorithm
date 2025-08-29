def test(graph):     
    for i in range(w):
        streak_zero = 0
        streak_one = 0
        is_streak = False
        for j in range(d):
            if graph[j][i] == 0:
                streak_zero += 1
                streak_one = 0

            else:
                streak_one += 1
                streak_zero = 0

            if streak_zero == k or streak_one == k:
                is_streak = True
                break

        if not is_streak:
            return 0
        
    return 1

def dfs(count, idx):
    global min_cnt
    if count >= min_cnt:
        return
    
    if test(graph):
        min_cnt = count
        return
    
    for i in range(idx, d):
        original = graph[i][:]

        graph[i] = [0]*w
        dfs(count+1, i+1)

        graph[i] = [1]*w
        dfs(count+1, i+1)

        graph[i] = original


t = int(input())
for tc in range(t):
    d,w,k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(d)]
    min_cnt = float("inf")

    if test(graph):
        print(f'#{tc+1} 0')
        continue

    dfs(0,0)
    print(f'#{tc+1} {min_cnt}')
