## 1
def solve():
    for a, b, c, d in calc[::-1]:
        if b == '-':
            tree[int(a)] = tree[int(c)] - tree[int(d)]
        elif b == '+':
            tree[int(a)] = tree[int(c)] + tree[int(d)]
        elif b == '/':
            tree[int(a)] = tree[int(c)] / tree[int(d)]
        elif b == '*':
            tree[int(a)] = tree[int(c)] * tree[int(d)]

for t in range(10):
    N = int(input())
    tree = [0] * 1001

    calc = []

    for _ in range(N):
        n = input().split()

        if len(n) == 2:
            tree[int(n[0])] = int(n[1])
        else:
            calc.append(n)
    
    solve()
    print(f'#{t+1} {int(tree[1])}')

## 2

T = 10

def postorder(node):
    if len(tree[node]) == 4: # 연산자 노드 (자식 2개)
        left = postorder(tree[node][2])
        right = postorder(tree[node][3])
        if tree[node][1] == '+':
            return left + right
        elif tree[node][1] == '-':
            return left - right
        elif tree[node][1] == '*':
            return left * right
        elif tree[node][1] == '/':
            return left / right
    else: # 리프 노드
        return int(tree[node][1])
    
for tc in range(1, T+1):
    N = int(input())
    tree = {}
    for _ in range(N):
        node = list(input().split())
        tree[node[0]] = node

    ans = postorder('1')
    print(f'#{tc} {int(ans)}')
