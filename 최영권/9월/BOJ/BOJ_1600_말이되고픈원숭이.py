from collections import deque
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

hr = [1, 2, 2, 1, -1, -2, -2, -1]
hc = [2, 1, -1, -2, -2, -1, 1, 2]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited= [[[0]*W for _ in range(H)] for _ in range(K+1)]
def monkey(k, r, c, dist):
    q = deque([(0, 0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        for _ in range(len(q)):
            k, r, c, dist = q.popleft()
            if r == H-1 and c == W-1:
                return dist
            
            if k<K:
                for dir in range(8):
                    nr, nc = r+hr[dir], c+hc[dir]
                    if nr<0 or nr>= H or nc<0 or nc>=W:
                        continue
                    
                    if not arr[nr][nc] and not visited[k+1][nr][nc]:
                        visited[k+1][nr][nc] = 1
                        q.append((k+1,nr,nc, dist+1)) 
                        
            
            for dir in range(4):
                nr, nc = r+dr[dir], c+dc[dir]
                if nr<0 or nr>=H or nc<0 or nc>=W:
                    continue
                
                if not arr[nr][nc] and not visited[k][nr][nc]:
                    visited[k][nr][nc] = 1
                    q.append((k,nr,nc, dist+1))
                    
    return -1
answer = monkey(0, 0, 0, 0)

print(answer)