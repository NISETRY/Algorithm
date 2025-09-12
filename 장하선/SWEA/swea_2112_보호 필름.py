# DFS 돌아서 통과여부 확인
def dfs():
    for i in range(w):
        film[]

def check():
    for i in range(w):
        cnt,tmp=0,1
        for j in range(h-1):
            if film[j][i]==film[j+1][i]:
                tmp+=1
            else:
                cnt=max(cnt,tmp)
                tmp=1
        cnt=max(cnt,tmp)
        if cnt<k:
            return
    return 0

T=int(input())
for tc in range(1,T+1):
    h,w,k=map(int,input().split())
    film=[0 for _ in range(h)]
    for i in range(h):
        film[i]=list(map(int,input().split()))
    initialcheck=check()
    # 약물 불필요한 경우
    if initialcheck==0:
        print(initialcheck)
    # 약먹자
    else:

