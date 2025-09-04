# 2시간 재고 풀어보기
# 생명력 x면 x시간동안 존버하구 x시간동안 번식함
# 번식으로 생성된 세포는 즉시 번식 가능
# 페트리 접시의 최대 크기만큼의 리스트를 미리 선언 : n+k//2-1, m+k//2-1 크기
from collections import deque
T=int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for tc in range(1,T+1):
    n,m,k=map(int,input().split())
    cells=[list(map(int,input().split())) for _ in range(n)]
    petry=[[0 for _ in range(m+k//2-1)] for _ in range(n+k//2-1)]
    visited=[[0 for _ in range(m+k//2-1)] for _ in range(n+k//2-1)]
    # petry에 담을 중간값 선언
    mid_row=(m+k//2-1)//2
    mid_col=(n+k//2-1)//2
    queue=deque()
    # petry에 cell 옮기기
    for i in range(n):
        for j in range(m):
            petry[mid_row-(m//2)+i][mid_col-(n//2)+j]=cells[i][j]
            if cells[i][j]!=0:
                queue.append((mid_row-(m//2)+i, mid_col-(n//2)+j, cells[i][j]))
                visited[mid_row-(m//2)+i][mid_col-(n//2)+j]=1
    # for i in range(len(petry)):
    #     print(petry[i])
    # 배양 시작
    # x+=1이 될때마다 liviing_petry의 data가 있는 영역의 숫자 감소
    # 그 부분의 원래 값의 절대값의 음수와 같아지는 경우 죽은 셀로 처리(-99)
    for x in range(k):
        for _ in range(len(queue)):
            x,y,life=queue.popleft()
            # print(x,y,life)
            # 비활성 상태
            if life>0:
                queue.append((x,y,life-1))
            # 활성 상태
            if life<=0:
                queue.append((x,y,life-1))
                new_life=petry[x][y]
                for d in range(4):
                    nx,ny=x+dx[d],y+dy[d]
                    if 0<=nx<m+k//2-1 and 0<=ny<n+k//2-1 and not visited[nx][ny]:
                        queue.append((nx,ny,new_life))
                        visited[nx][ny]=1
            # 세포 죽음 ㅠ
            if life==-abs(petry[x][y]):
                petry[x][y]=-99
    print(f'#{tc} {len(queue)}')