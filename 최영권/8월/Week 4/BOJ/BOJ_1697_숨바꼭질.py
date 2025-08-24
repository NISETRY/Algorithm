from collections import deque
N, K = map(int, input().split())

time = 0
visited = set([N])
possible_position = deque([N])

while possible_position:
    
    for i in range(len(possible_position)):
        cur_pos = possible_position.popleft()
        if cur_pos == K:
            print(time)
            exit(0)
        for nxt in [cur_pos-1, cur_pos+1, 2*cur_pos]:
            if nxt not in visited and 0<=nxt<=100000:
                visited.add(nxt)
                possible_position.append(nxt)
        
    time += 1