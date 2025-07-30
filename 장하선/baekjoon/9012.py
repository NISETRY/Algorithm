n=int(input())
def ps(x):
    before_vps=[0,0]
    after_vps=before_vps.copy()
    for i in range(len(x)):
        if x[i]=='(':
            after_vps[0]+=1
        else:
            after_vps[1]+=1
        if after_vps[0]!=after_vps[1]:
            before_vps=after_vps.copy()
        elif before_vps[0]>before_vps[1]:
            before_vps=[0,0]
            after_vps=before_vps.copy()
        else:
            return 'NO'
    return 'YES' if after_vps[0]==after_vps[1] else 'NO'
for _ in range(n):
    x=input()
    print(ps(x))