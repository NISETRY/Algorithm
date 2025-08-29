n,m,x,y,k=map(int,input().split())
zido=[list(map(int,input().split())) for _ in range(n)]
upper_dice=[]
dice=[]
# dir=1,2이면 사이드로 이동, 그 외는 위 아래로 이동

for i in range(k):
