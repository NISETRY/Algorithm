from collections import deque
A, P = map(int, input().split())

q = deque([A])
while True:
    cur_num = q[-1]
    next_num = 0
    for i in range(len(str(cur_num))):
        next_num += (int(str(cur_num)[i]) ** P)
    if next_num not in q:
        q.append(next_num)

    else:
        print(q.index(next_num))
        break
    