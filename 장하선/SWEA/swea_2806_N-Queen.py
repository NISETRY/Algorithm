# 풀이 2(강사님 풀이)
T=int(input())

def n_queen(row): # row는 겹칠 일 없으니까 row로 변수명 선언
    global ans

    if row==n: # n개의 퀸을 무사히 배치하면 재귀 탈출
        ans+=1
        return
    
    for col in range(n): # 열을 고를 예정
        # 세로 검사 통과 + 좌하향 + 우하향 대각선을 모두 통과
        # visited_col[col], visited_main_diag[col], visited_sub_diag[col]이 미방문 상태이면 통과
        if not visited_col[col] and not visited_main_diag[row-col+n-1] and not visited_sub_diag[row+col]: 
            visited_col[col]=1
            visited_main_diag[row-col+n-1]=1
            visited_sub_diag[row+col]=1
            
            n_queen(row+1) # 3개 조건에서 모두 미방문이면 다음 퀸을 배치

            # 배치가 끝났으면 visited를 원복시킴
            visited_col[col]=0
            visited_main_diag[row-col+n-1]=0
            visited_sub_diag[row+col]=0

for tc in range(1,T+1):
    n=int(input())

    visited_col=[0]*n # 행 visited
    visited_main_diag=[0]*(2*n-1) # 주대각선 visited
    visited_sub_diag=[0]*(2*n-1) # 부대각선 visited
    ans=0 # 답으로 출력할 변수
    
    n_queen(0)
    print(f'#{tc} {ans}')

# 풀이 1

# 퀸이 있는 현 위치 가준으로 같은 행,열,대각은 안되는 것
# 행 or 열은 1차원 배열로 받고, 
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    # 행 기준으로 입력 점검, 0은 아직 퀸 배치 안된 것
    row=[0 for _ in range(n)]
    # 가능한 경우의 수 counting, 답으로 출력 예정
    cnt=0
    # 가지치기로 불능해를 미리 제거
    def pruning(x):
        # 퀸을 배치하고, 불능해이면(공격받는 경우) False 반환, 아직 가능하면 True를 반환
        # 뒤의 queen 함수에서 n개의 퀸을 1개, 2개, ...으로 배치할 때 계속해서 사용할 예정
        for i in range(x):
            if row[i]==row[x] or abs(row[x]-row[i])==x-i:
                return False
        return True
    def queen(x):
        # 가능한 해를 구한 경우는 전역 변수는 cnt를 1개씩 증가시켜야 하므로 global 변수 선언
        global cnt
        # n개의 퀸이 이상 없이 배치되었다면 cnt 1개 증가
        if x==n:
            cnt+=1
            return
        # n개의 퀸을 배치해보기
        for i in range(n):
            # 퀸을 배치한 위치에 0->i로 치환시켜 퀸이 있음을 알림
            # 이는 위의 pruning 함수에서 대각선 확인 시에 사용
            row[x]=i
            # pruning이 True일 시 그 다음 퀸을 배치
            # 이를 n번 수행해서 n개 퀸이 모두 배치된다면 cnt+=1
            if pruning(x):
                queen(x+1)
    queen(0)
    print(f'#{tc} {cnt}')