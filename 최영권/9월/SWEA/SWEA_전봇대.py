T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        start, end = map(int, input().split())
        lst.append((start, end))
    lst.sort(key = lambda x : x[0])
    count = 0 
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] > lst[j][1]:
                count += 1 
    print(f"#{tc} {count}")