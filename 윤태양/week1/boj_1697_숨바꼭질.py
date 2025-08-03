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
    que = [[n]]
    
    while True:
        a = que.pop(0)
        last = a[-1]
        if last ==k:
            return a
        move = act(last)

        for i in move:
            if i not in visited:
                visited.append(i)
                temp = []
                for j in range(len(a)):
                    temp.append(a[j])
                temp.append(i)
                que.append(temp)
                
print(len(bfs(n))-1)
                                
        
        