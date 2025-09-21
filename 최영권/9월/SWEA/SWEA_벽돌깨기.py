# 1. 최소 벽돌
# - 현재 벽돌이 다 깨지면 더 이상 할 필요 X -> 현재 벽돌 수를 관리


# N번의 구슬을 굴려야 한다
# - 모든 케이스를 보아야한다 -> 약 25만번 ( 12 ^ 4 ) 

# - 백트래킹
    # - 한 번 쏘면 벽돌들이 연쇄적으로 깨져야한다
    # - 현재 기준으로 퍼져나가면서 탐색(BFS)
    # - 빈칸 메우기
from collections import deque
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
def shoot(cnt, remains, now_arr):
    global min_blocks

    # 종료조건 : N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 모든 열에 한 번씩 떨어트리자
    for col in range(W):
        # 방법1. 원본을 복사해두고, 다시 되돌리는 방법
        # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
        # 2. 원본 리스트의 col위치에 떨구고
        # 3. cnt + 1번 재귀 상태로 이동
        # 4. 떨구기 전 상태로 복구

        # 방법2. 복구시간이 없는 방식
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col위치에 떨군다
        # 3. cnt + 1번 상태로 이동할 때, copy_arr을 함께 전달
        copy_arr = [row[:] for row in now_arr]


        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        # 벽돌이 없는 열은 pass
        if row == -1:  
            continue
        
        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행,열, 숫자를 모두 담아야한다
        q = deque([(row,col,copy_arr[row][col])])
        now_remains = remains - 1
        copy_arr[row][col] = 0
        # 주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p칸을 모두 제거
            for k in range(1,p):
                for i in range(4):
                    nx = r + dy[i]*k
                    ny = c + dx[i]*k
                    # 범위 밖이면 pass
                    if nx<0 or nx >= H or ny < 0 or ny >= W:
                        continue   
                    # 벽돌이 없으면 pass
                    if copy_arr[nx][ny] == 0:
                        continue
                    q.append((nx, ny, copy_arr[nx][ny]))  # 다음 벽돌 추가
                    copy_arr[nx][ny] = 0                  # 벽돌 깨짐
                    now_remains -= 1                      # 숫자 감소
        # 빈칸을 메워주는 코드
        for c in range(W):
            idx = H - 1 # 벽돌이 위치할 index
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(cnt + 1, now_remains, copy_arr)

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    
    min_blocks = 1e9
    # 남은 벽돌 수
    blocks = 0
    
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1


    shoot(0, blocks, arr)
    print(f"#{tc} {min_blocks}")