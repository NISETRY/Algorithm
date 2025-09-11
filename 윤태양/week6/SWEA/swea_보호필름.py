def test(graph):     
    for i in range(w):
        now = -1
        streak = 0
        is_streak = False
        for j in range(d):
            if graph[j][i] == now:
                streak += 1
            else:
                now = graph[j][i]
                streak = 1
  
            if streak == k:
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