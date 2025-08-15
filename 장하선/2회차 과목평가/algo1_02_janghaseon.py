T=int(input())

for tc in range(1,T+1):
    n,m,k=map(int, input().split())
    # 입력 받기
    space=[[] for _ in range(n)]
    for _ in range(n):
        lst=input()
        for x in range(len(lst)):
            space[_].append(lst[x])
    # 로직 : n-m 구간에서 다 찾기
    # flag를 통해 조건을 만족하는 경우에만 특정 행위를 수행하게 함
    flag=False
    for x in range(n-m+1):
        for y in range(n-m+1):
            stars=0
            # m*m크기 안을 확인하고 * 찾기
            for i in range(m):
                for j in range(m):
                    if space[x+i][y+j]=='*':
                        stars+=1
            # stars가 정확히 k개인 경우 flag 바꿔줌
            # 별도의 값에 조건을 만족했던 x,y 좌표를 저장해주고 변경하지 않음
            if stars==k:
                flag=True
                a,b=x,y
    if flag:
        print(f'#{tc} {a} {b}')
    else:
        print(f'#{tc} {-1} {-1}')