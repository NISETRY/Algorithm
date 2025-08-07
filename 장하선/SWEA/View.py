t=0
while True:
    try:    
        n=int(input())
        buildings=list(map(int,input().split()))
        view=0
        for i in range(2,n-2):
            view_build=buildings[i-2:i+3]
            high=max(view_build)
            if view_build[2]==high:
                view_build.remove(high)
                view+=high-max(view_build)
        t+=1
        print(f'#{t} {view}')
    except EOFError:
        break