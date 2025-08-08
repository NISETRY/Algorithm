T=int(input())
for tc in range(1,T+1):
    steel=input()
    cnt,res=0,0 # cnt : 막대수, res : 출력
    # (( : 막대 추가
    # )) : 막대 끊김
    # () : 레이저 발사
    # )( : 막대 끊겼다가 다시 생김
    for i in range(len(steel)):
        if steel[i]=='(':  
            cnt+=1
        if steel[i]==')': # 막대 절단이 필연적으로 발생하는 구간, '()'이면 레이저 발사됨
            if steel[i-1]=='(':
                res+=cnt-1
            else: # '끊겼다가' 생겼으니까 res+=1
                res+=1
            cnt-=1
    print(f'#{tc} {res}')