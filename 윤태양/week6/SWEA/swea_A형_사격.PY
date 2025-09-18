import time
start_time = time.time()

def bang2(graph):
    if graph[0] > graph[1]:
        return 2*graph[0]
    
    else:
        return 2*graph[1]

def bang(target, graph, score):
    if len(graph) <= 2:
        score += bang2(graph)

    if len(graph)>=3 and target != 0 and target != len(graph)-1:
        score += graph[target-1] * graph[target+1]

    if len(graph)>=3 and target == 0:
        score += graph[target+1]

    if len(graph)>=3 and target == len(graph):
        score += graph[target-1]

    graph.pop(target)
    return score


def dfs(count, graph, score):
    global answer
    pre = score    
    if pre > answer:
        answer = pre

    if count == n-1:
        return
    
    for i in range(0, len(graph)):
        og_graph = graph[:]
        new_score = bang(i, graph, pre)
        dfs(count+1, graph, new_score)
        graph = og_graph


t = int(input())

for tc in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    answer = 0
    dfs(0,graph,0)
    dp = {[]*n}

    print(f'#{tc+1} {answer}')


# 풍선 터트리는 함수
# dfs 

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산

print(f"Execution time: {elapsed_time} seconds")