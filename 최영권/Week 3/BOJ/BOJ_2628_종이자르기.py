N, M = map(int, input().split())
cut = int(input())

rowcut = [0, M]
colcut = [0, N]
for _ in range(cut):
    d, num = map(int, input().split())
    
    if d == 0:
        rowcut.append(num)
    elif d == 1:
        colcut.append(num)


rowcut.sort()
colcut.sort()

max_h = max(rowcut[i+1] - rowcut[i] for i in range(len(rowcut)-1))
max_w = max(colcut[i+1] - colcut[i] for i in range(len(colcut)-1))
print(max_h, max_w)
