for tc in range(10):
 
    N = int(input())
 
    l = list(map(int, input().split()))
 
    result = []
 
    for i in range(2, N-2):
        a = max(l[i-2], l[i-1], l[i+1], l[i+2])
        if l[i] > a:
            b = l[i]-a
            result.append(b)
 
    print(f'#{tc+1} {sum(result)}')