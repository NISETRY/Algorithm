T = int(input())

def check_cycle(idx):
    global count
    global visited

    visited.append(idx)
    if graph[idx] in visited:
        count += 1
    else:
        check_cycle(graph[idx])
    return count



for tc in range(1, T+1):
    count = 0
    visited = []
    N = int(input())
    graph = list(map(int, input().split()))
    graph.insert(0, 0)
    for i in range(1, len(graph)):
        if i not in visited:
            check_cycle(i)
            # print(i, visited, count)
    
    print(count)
    