def comb(count, idx):
    if count == 6:
        pick.append(temp[:])
        return
    
    for i in range(len(graph)):
        if i>idx and graph[i] not in temp:
            temp.append(graph[i])
            comb(count+1, i)
            temp.pop()

while True:
    graph = list(map(int, input().split()))
    if len(graph) == 1 and graph[0] == 0:
        break

    temp = []
    pick = []

    comb(0,0)
    for i in pick:
        print(*i)
    print()