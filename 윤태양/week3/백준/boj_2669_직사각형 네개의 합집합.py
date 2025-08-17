graph = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for r in range(x1, x2):
        for c in range(y1, y2):
            graph[r][c] = 1

sum_graph = 0
for i in graph:
    sum_graph += sum(i)
print(sum_graph)