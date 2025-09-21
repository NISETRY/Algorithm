# 그룹이 연결된 것인지 확인하기
def connect(group, nearby):
    # 공집합은 False
    if not group:
        return False
    # 두 그룹이 모두 면결된 그룹인지를 확인
    group_set=set(group)
    sp=group[0]
    # visited를 집합으로 처리
    seen={sp}
    queue=deque([sp])
    while queue:
        x=queue.popleft()
        for i in group_set:
            if i not in seen and nearby[x][i]==1:
                seen.add(i)
                queue.append(i)
    # 중복 방문했다면 group_set이랑 seen의 길이 차이가 생김
    # 길이 차이가 있다 == 연결된 그룹이 아니다
    return len(seen)==len(group_set)

# 분할 체크 및 계산
def gary(team):
    # 팀 나누기
    red=[i for i in range(1,n+1) if not team[i]]
    blue=[i for i in range(1,n+1) if team[i]]
    # 연결 안되어있거나 공집합이면 꺼버림
    if not red or not blue or not connect(red, nearby) or not connect(blue, nearby):
        return
    # 연결된 선거구라면 인구수 체크
    red_party=[population[i] for i in red]
    blue_party=[population[i] for i in blue]
    return abs(sum(red_party)-sum(blue_party))

# 생성 가능한 모든 부분집합 만들기
def dfs(idx, team, tupyo):
    global ans
    # tupyo만큼 고르면 check에 있는 선거구 현황을 gary로 검산
    if team == tupyo:
        diff = gary(check)
    # None이 나오지 않으면(연결이 유효하다면) gary에서 나온 답과 현재 답 간의 최솟값을 비교
        if diff is not None:
            ans = min(ans, diff)
        return
    # 선거구를 고르는 로직
    for x in range(idx, n+1):
        check[x] = 1
        dfs(x+1, team+1, tupyo)
        check[x] = 0
# 입력 및 로직 수행
from collections import deque
n=int(input())
population=[0]+list(map(int,input().split()))
nearby=[[0 for _ in range(n+1)] for _ in range(n+1)]
res=-1
for i in range(n):
    near=list(map(int,input().split()))
    for j in near[1:]:
        nearby[i+1][j]=nearby[j][i+1]=1
# pruning / n==2이면 서로 연결되어있지 않더라도 분리가 진행되었으니 볼 필요 없음
if n==2:
    print(abs(population[2]-population[1]))
    flag=False
else:
    ans=float('inf')
    check=[0]*(n+1)
    for size in range(1, n//2 + 1):
        dfs(1, 0, size)
    print(ans if ans != float('inf') else -1)