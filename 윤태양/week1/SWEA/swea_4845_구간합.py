n = int(input())
 
for i in range(n):
    a, b = map(int, input().split())  # size / 구간합 크기 
    l = list(map(int, input().split()))
    min1, max1 = 10000000000000, -1
 
    for j in range(a-b+1):
        hap = 0
        for k in range(j, j+b):
            hap += l[k]
                 
        min1 = min(min1,hap)
        max1 = max(max1,hap)
 
    print(f'#{i+1} {max1 - min1}')
 
# i = 3
# a, b = 10, 3
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]