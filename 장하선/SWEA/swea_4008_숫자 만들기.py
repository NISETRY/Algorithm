import sys
sys.stdin=open('input.txt')

max_res=-999999999
min_res=9999999999

def calculator(a,b,op):
    if op=='+': return a+b
    elif op=='-': return a-b
    elif op=='*': return a*b
    else: return int(a/b)

def dfs():
    if len(pick)==n:
        pre_op.append(tuple(oper[i] for i in pick))
        return
    seen=set()
    for i in range(n):
        if i in pick:
            continue
        op_tmp=oper[i]
        if op_tmp in seen:
            continue
        seen.add(op_tmp)
        pick.append(i)
        dfs()
        pick.pop()

T=int(input())
for tc in range(1,T+1):
    n=int(input())-1
    op=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    oper,pick,pre_op=[],[],[]
    for i in range(4):
        if i==0:
            for j in range(op[i]):
                oper.append('+')
        elif i==1:
            for j in range(op[i]):
                oper.append('-')
        elif i==2:
            for j in range(op[i]):
                oper.append('*')
        elif i==3:
            for j in range(op[i]):
                oper.append('/')
    dfs()
    
    for x in range(len(pre_op)):
        a=nums[0]
        for y in range(n):
            b=nums[y+1]
            a=calculator(a,b,pre_op[x][y])
        if a>max_res: max_res=a
        if a<min_res: min_res=a
    print(f'#{tc} {max_res-min_res}')