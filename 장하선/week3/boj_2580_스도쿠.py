import pprint



sudo=[0]*9
sudo_check=[0]*10
for i in range(9):
    sudo[i]=list(map(int, input().split()))
    # 세로줄 입력 받으면서 0이 하나만 있으면 그거 채워주기
    if sudo[i].count(0)==1:
        idx=sudo[i].index(0)
        k=sum(sudo[i])
        sudo[i][idx]=45-k
# 이후 가로줄에 0이 하나만 있는 경우 확인 후 채워주기
for i in range(9):
    cnt,k=0,0
    for j in range(9):
        k+=sudo[j][i]
        if sudo[j][i]==0:
            cnt+=1
            idx=j
        if cnt>1:
            break
    if cnt==1:
        sudo[idx][i]=45-k
pprint.pp(sudo)