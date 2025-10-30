n, m = map(int, input().split()) # 그래프 크기, 택배 개수
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    k, h, w, c = map(int, input().split()) # 번호, 세로크기, 가로길이, c 왼쪽 위 위치
                                           # c, c+w까지 싹다 0이면 아래로 하강 
                                           # 택배는 싹다 택배번호로 채워놓고
                                           # 높이는 어차피 0에서 시작
                                           # 아래로 하강할 때마다 높이 +1해서 n까지 or n-h까지
    
    
    
    

# 다 빼고 난뒤
# 오른쪽 빼고 하강 
# 왼쪽 빼고 하강
# 순서 기록 -> 끝