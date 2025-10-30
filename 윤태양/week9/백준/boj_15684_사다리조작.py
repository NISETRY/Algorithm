n, m, h = map(int, input().split()) # 세로선, 가로선, 세로선마다 놓을 수 있는 가로선 개수 
lines = [list(map(int ,input().split())) for _ in range(m)] # b번, b+1번 세로선을 a에서 연결
graph = [[0]*n for _ in range(h)]

for a, b in lines:
    graph[a-1][b-1] = 1
    graph[a-1][b] = 1

def sadari(i):
    r, c = 0,i

    while r < h:
        if c < n - 1 and graph[r][c] == 1:
            c += 1 
        
        elif c > 0 and graph[r][c-1] == 1:
            c -= 1

        r += 1

    if c == i:
        return True
    return False

for i in range(n):
    print(sadari(i))
