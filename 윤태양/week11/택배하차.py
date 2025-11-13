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
                break
                
        if can_drop:
            pos += 1
    
    for i in range(h):
        for j in range(w):
            graph[pos+i][j+c] = k
            
def left_off():
    global rest_list
    left = [0 for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[c][r] != 0 and left[r] == 0:
                left[r] = graph[c][r]
    
    
    hubo_count = [0 for _ in range(m+2)]
    for i in left:
        hubo_count[i] += 1
        
    real_hubo= []        
    for a in range(1, len(hubo_count)-2):
        if verify[a] == hubo_count[a]:
            real_hubo.append(a)
            
    real_hubo.sort()
    hubo = real_hubo.pop(0)
    answer.append(hubo)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == hubo:
                graph[i][j] = 0
                
    rest_list = [(k, h, w, c) for k, h, w, c in rest_list if k != hubo]
            
    for k1, h1, w1, c1 in rest_list:
        drop(k1, h1, w1, c1, 0)
        
def right_off():
    global rest_list
    right = [0 for _ in range(n)]
    for r in range(n):
        for c in range(n-1,-1,-1):
            if graph[c][r] != 0 and right[r] == 0:
                right[r] = graph[c][r]
    
    
    hubo_count = [0 for _ in range(m+2)]
    for i in right:
        hubo_count[i] += 1
        
    real_hubo= []        
    for a in range(1, len(hubo_count)-2):
        if verify[a] == hubo_count[a]:
            real_hubo.append(a)
            
    real_hubo.sort()
    hubo = real_hubo.pop(0)
    answer.append(hubo)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == hubo:
                graph[i][j] = 0
                
    rest_list = [(k, h, w, c) for k, h, w, c in rest_list if k != hubo]
            
    for k1, h1, w1, c1 in rest_list:
        drop(k1, h1, w1, c1, 0)
        
    


n, m = map(int, input().split()) # 그래프 크기, 택배 개수
graph = [[0]*n for _ in range(n)]
verify = {}
rest_list = []
answer = []
for _ in range(m):
    k, h, w, c = map(int, input().split()) # 번호, 세로 크기, 가로 크기, 좌측 좌표
    c -= 1
    rest_list.append((k,h,w,c))
    verify[k]= h
    drop(k,h,w,c,0)
    
while len(answer) != m:
    left_off()
    right_off()
    print("실행")

for i in range(len(answer)):
    print(answer[i])

