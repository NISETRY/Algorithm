t = int(input())

for tc in range(t):
    p, pa, pb = map(int, input().split())
    al, ar, bl, br = 1, p, 1, p
    ac, bc = -1, -1
    while True:
        if ac == pa and bc == pb:  # 탈출조건 같을 때를 무조건 먼저 검사
            ans = 0
            break
        elif ac == pa:             # A 먼저 도달
            ans = 'A'
            break
        elif bc ==pb:              # B 먼저 도달
            ans = 'B'
            break
            
        ac = int((al+ar)/2) # 센터계산
        bc = int((bl+br)/2)
        
        if ac < pa:         # 오른쪽, 왼쪽을 센터로 이동
            al = ac
        else:
            ar = ac
            
        if bc < pb:
            bl = bc
        else:
            br = bc
        # print(ar, al, br, bl)
            
    print(f'#{tc+1} {ans}')
    