# 홀수일에는 1 증가, 짝수일에는 2 증가 -> 모듈러 사용
# 하루에 한 나무에만 물을 줄 수 있음
# 전략 : 두 번째로 큰 나무에 물을 주는데, 이 나무와 목표 나무의 키 차이가 1인지 2인지에따라 3번 나무에 물 줄지 여부 결점
T=int(input())
for tc in range(1, T+1):
    n = int(input())
    trees = list(map(int, input().split()))
    val_aim = max(trees)
    water=[]
    water_1=[]
    water_2=[]
    for i in range(n):
        water.append(val_aim-trees[i])
    flag = False
    days=sum(water)
    for i in range(n):
        water_1.append((water[i]//3)+1 if water[i]%3==1 else 0)
        water_2.append((water[i]//3)+1 if water[i]%3==2 else 0)
    # 초기값이 모두 같은 높이의 나무면 물 줄 필요 없으니까 0 리턴할 계획
    if days==0:
        res = 0
        flag = True
    if not flag:
        for i in range(n):
            if sum(water_1)-sum(water_2)>1:
                res=2*sum(water_1)-1
            elif sum(water_2)-sum(water_1)>1:
                res=2*sum(water_2)
            else:
                res=sum(water_1)+sum(water_2)
    print(f'#{tc} {res}')

