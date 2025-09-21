T = int(input())

def dfs(r, c, word):
    if len(word) == 7:
        if word not in answer:
            answer.add(word)
        return
    for dr, dc in [(1,0), (-1, 0), (0,1),(0,-1)]:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            continue
        dfs(nr, nc, word+arr[nr][nc])

# T = 1
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]   
    # arr = [['1','1','1','1'], ['1','1','1','2'],['1','1','2','1'],['1','1','1','1']]
    answer = set()
    for i in range(4):
        for j in range(4):
            word = ''
            dfs(i, j, word)
    answer = set()
    for i in range(4):
        for j in range(4):
            word = ''
            dfs(i, j, word)
    print(f"#{tc} {len(answer)}")