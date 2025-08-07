T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    sumlst = []
    for i in range(N-M+1):
        for j in range(N-M+1):
                        
            sum = 0
            for r in range(i,i+M):
                for c in range(j, j+M):
                    sum += arr[r][c]
                    sumlst.append(sum)
    print(f"#{tc} {max(sumlst)}")

