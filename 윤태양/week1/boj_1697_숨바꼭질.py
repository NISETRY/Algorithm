from collections import deque
k, n = map(int, input().split())
visited = []

def act(n):
    move1 = int(n/2)
    move2 = n+1
    move3 = n-1
    if n%2==0:
        return [move1,move2,move3]
    else:
        return [move2,move3]

def bfs(n):
    visited.append(n)
    que = deque()
    que.append([n])
    
    while True:
        a = que.popleft()
        last = a[-1]
        if last ==k:
            print(a)
            return a
        move = act(last)

        for i in move:
            if i not in visited:  # O(n)
                visited.append(i) # O(1)
                temp = a.copy() # O(n)
                temp.append(i)  # O(1)
                que.append(temp)
if k>=n:
    print(k-n)
else:
    print(len(bfs(n))-1)
                                
        
        