N = int(input())
n = list(range(1, N + 1))

num = list(map(int, input().split())) # 해당 구역의 인구수

# 인접 리스트
l = [[] for _ in range(N+1)]

for i in range(1, N+1):
    a = list(map(int, input().split()))
    l[i].extend(a[1:])

# 인접 리스트를 이용해서 연결되어 있는 형태인지 확인하는 함수
def is_connected(group, l):
    visited = set()

    stack = [group[0]]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            for n in l[node]:
                if n in group and n not in visited:
                    stack.append(n)

    # 연결된 노드 수 == 그룹 전체 노드 수
    return len(visited) == len(group)

picked = []
answer = float('inf')

def comb(count, idx):
    global answer
    if 1 <= count <= N // 2:
        g1 = picked[:]
        g2 = [x for x in n if x not in picked]
        
        if is_connected(g1, l) and is_connected(g2, l):
            sum_g1 = sum(num[i-1] for i in g1)
            sum_g2 = sum(num[i-1] for i in g2)

            diff = abs(sum_g1 - sum_g2)
            if diff < answer:
                answer = diff
   
    if count == N // 2:
        return
    
    for i in range(idx, N):
        picked.append(n[i])
        comb(count + 1, i + 1)
        picked.pop()

comb(0,0)

if answer == float('inf'):
    print(-1)  # 불가능한 경우
else:
    print(answer)