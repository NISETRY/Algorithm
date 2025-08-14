# input
n,m=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(n)]

ck=[] # 치킨집 좌표 저장
home=[] # 집 좌표 저장

# 계획
# 1. 단 집과 치킨간의 거리를 전부 구해
# 2. 집 개수*치킨집 개수의 행렬 만들고 그 행렬 안에 '치킨 거리' 저장
# 3. m개 치킨집에 대해 치킨 거리 합이 최소가 되는 경우 구하기(조합?)
    
# 조합 함수 응용해서 살릴 치킨집 후보 만들기
def comb(cnt, idx):
    global safe
    if len(nCm)==m:
        safe.extend(nCm)
        return
    for i in range(idx, len(cand)):
        nCm.append(cand[i])
        comb(cnt+1, i+1)
        nCm.pop()

# 치킨 거리 저장을 위한 사전 작업
for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            ck.append((i,j))
        elif city[i][j]==1:
            home.append((i,j))

# 모든 치킨 거리 저장
ck_lens=[[0 for _ in range(len(home))] for _ in range(len(ck))]
for x in range(len(ck)):
    for y in range(len(home)):
        ck_lens[x][y]=abs(ck[x][0]-home[y][0])+abs(ck[x][1]-home[y][1])

nCm=[] # 폐업 안시킬 치킨집 위치를 임시로 저장하기 위한 배열
safe=[] # 폐업 안시킬 치킨집 위치를 모두 저장하기 위한 배열
comb(0,0) # 치킨집 저장
res=99999999 # 답으로 나올 변수 미리 선언

for i in range(0,len(safe),m):
    min_ck_len=[] # 살릴 치킨집에 해당하는 행을 저장할 배열 선언
    for j in range(i,i+m):
        min_ck_len.append(ck_lens[safe[j]])
    distance=[9999]*(len(home)) # 치킨 거리 최솟값 비교하기 위한 배열
    for y in range(len(home)):
        for x in range(m):
            if distance[y]>min_ck_len[x][y]: # 저장되었던 변수가 더 크면 변수 갱신
                distance[y]=min_ck_len[x][y]
    res=min(res,sum(distance)) # 저장한 변수의 합이 더 작은 경우에 변수 갱신
print(res) # 최종 결과값 출력
