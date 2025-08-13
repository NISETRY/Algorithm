i=input
def p(n):
    if n==1:return 1
    elif n==2:return 3
    else:return p(n-1)+2*p(n-2)
T=int(i())
for t in range(T):
    k=int(i())//10
    print(f'#{t+1} {p(k)}')