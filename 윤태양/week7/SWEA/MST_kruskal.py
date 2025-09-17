v, e = map(int, input().split())
edges = []
for _ in range(e):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])

count = 0  # 현재까지 선택한 간선의 수
result = 0 # 가중치의 합

parents = [i for i in range(v)] # make_set

def find_set(x):
    if x == parents[x]: # 내가 나의 부모?
        return x
    
    parents[x] = find_set(parents[x]) 
    return parents[x] 

def union(x,y):
    rx, ry = find_set(x), find_set(y)

    if rx == ry: # 사이클 발생
        return
    if rx<ry:
        parents[ry] = rx
    else:
        parents[rx] = ry
    


for u,v,w in edges:
    
    if find_set(u) != find_set(v):
        union(u,v)
        count += 1
        result += w

        if count == v-1:
            break

print(result)


