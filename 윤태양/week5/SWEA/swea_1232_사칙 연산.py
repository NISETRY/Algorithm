def post_order(n):
    if left[n] != 0 or right[n] != 0:
        x = post_order(left[n])
        y = post_order(right[n])

        if tree[n] == '-':
            return x-y
        
        elif tree[n] == '+':
            return x+y

        elif tree[n] == '*':
            return x*y

        elif tree[n] == '/':
            return x/y

    else:
        return tree[n]

for tc in range(10):
    n = int(input())
    tree = [0]*(n+1)
    left = [0]*(n+1)
    right = [0]*(n+1)

    for i in range(n):
        node = input().split()

        if len(node) == 4:
            tree[int(node[0])] = node[1]
            left[int(node[0])] = int(node[2])
            right[int(node[0])] = int(node[3])

        else:
            tree[int(node[0])] = int(node[1])

    answer = int(post_order(1))
    print(f'#{tc+1} {answer}')