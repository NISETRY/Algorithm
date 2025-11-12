from pprint import pprint

def drop(k,h,w,c,pos):
    global graph
    
    can_drop = True
    
    while can_drop:
        for width in range(w):
            if pos+h<n and graph[pos+h][c+width] == 0:
                pass 
            else:
                can_drop = False
                
        if can_drop:
            pos += 1
    
    for i in range(h):
        for j in range(w):
            graph[pos+i][j+c] = k
            
def left_off():
    left = [0 for _ in range(1,m+1)]
    for 
    


n, m = map(int, input().split()) # 그래프 크기, 택배 개수
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    k, h, w, c = map(int, input().split()) # 번호, 세로 크기, 가로 크기, 좌측 좌표
    c -= 1
    drop(k,h,w,c,0)
    
    pprint(graph)