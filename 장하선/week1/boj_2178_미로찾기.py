n,m=map(int,input().split())
maze=[[] for _ in range(n)]
visited=[[0,0]]
queue=[[0,0]]
for i in range(n):
    k=input()
    for j in range(m):
        maze[i].append(int(k[j]))
# 현 위치 x,y에 대해 이동 가능한 경우는 x+-1, y+-1 4개
# 이미 방문한 인덱스는 빈 리스트에 저장
# 막다른 길인 경우, pop으로 해당 리스트 반환 후 백트래킹
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while queue:
    x,y=map(int, queue.pop())
    
print(len(queue))