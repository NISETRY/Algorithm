import pprint
N, M = map(int, input().split())
arr = []
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == "R":
            red_r, red_c = i, j
        if tmp[j] == "B":
            blue_r, blue_c = i, j
        if tmp[j] == "O":
            fr, fc = i, j
        arr.append(tmp)
# 4방향 기울이기 
# 10번이내에 파란공이 들어가지 않으면서 빨간 공이 O만나서 들어가면 1 아니면 0

# 10번을 돌면서 
# 한번 기울일때 마다 4방향의 맵 저장 -> 현재랑 그대로면 폐기
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# c가 0이먄 N을 봐야되고, r이 0이면 M을 봐야대
def roll(map):
    for d in range(4):
    # 빨간공 위치, 파란공 위치 조정
        nr, nc = red_r+dr[d], red_c+dc[d]
        arr[red_r][red_c] = "."
        while arr[nr][nc] == '.':
            nr, nc = nr+dr[d], nc+dc[d]
            if arr[nr][nc] == "#":
                break
            if arr[nr][nc] == "O":
                break              
        br, bc = blue_r+dr[d],blue_c+dc[d]
        arr[blue_r][blue_c] = "."
        while arr[nr][nc] == '.':
            nr, nc = nr+dr[d], nc+dc[d]
            if arr[nr][nc] == "#":
                break
            if arr[nr][nc] == "O":
                break        
        arr[br][bc] = 'B'        
        arr[nr][nc] = 'R'
        pprint.pprint(arr)

    return 
count = 0
answer = 1
while count < 10:
    roll(arr) # roll결과가 map이랑 다른 경우만 가져오기
    if (blue_r, blue_c) == (fr, fc):
        answer = 0
        break
    count += 1





