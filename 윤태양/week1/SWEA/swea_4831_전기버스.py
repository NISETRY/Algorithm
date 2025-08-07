t = int(input())
 
for i in range(t):
    k, n, m = map(int, input().split())
    m_list = list(map(int, input().split()))
 
    last = 0
    stop = 0
    energy = k
    now = 0
    for_break = False
 
    while now != n:
        now+=1
        energy-=1
 
        if energy == 0:
            if now == n:
                break
             
            while now not in m_list:
                now-=1
 
            if last == now:
                for_break = True
                break
             
            energy=k
            stop+=1
            last = now
 
    if for_break == True:
        print(f'#{i+1} 0')
    else:
        print(f'#{i+1} {stop}')