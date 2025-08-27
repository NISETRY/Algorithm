temp = []
pick = []

def comb(count, idx):
    pick.append(temp[:])
    if count == n:
        return
    
    for i in range(1, n+1):
        if i>idx:
            temp.append(graph[i])
            comb(count+1, i)
            temp.pop()

n, s = map(int, input().split())
graph = [0] + list(map(int, input().split()))
cnt = 0 

comb(0,0)

for i in pick[1:]:
    if sum(i) == s:
        cnt+=1

print(cnt)