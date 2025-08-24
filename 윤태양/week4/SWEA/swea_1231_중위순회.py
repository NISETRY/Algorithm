
def in_order(T, i=1):
    if  i >= len(graph) or graph[i] == None:
        return
    
    in_order(graph, i*2) 
    res.append(graph[i])  
    in_order(graph, i*2 + 1)

    return res


for tc in range(10):
    res = []    
    n = int(input())
    graph = [0] * (n+1) 
    for i in range(1, n+1):
        temp = list(input().split())
        graph[i] = temp[1]

    in_order(graph)
    print(f'#{tc+1} ', *res, sep='')