x, y = map(int, input().split())
N = int(input())

h = [0, y]
w = [0, x]
result = []

for _ in range(N):
    a, b = map(int, input().split())

    # 0 가로, 1 세로 
    if a == 0:
        h.append(b)

    elif a == 1:
        w.append(b)

w.sort()
h.sort()

for i in range(len(w)-1):
    for j in range(len(h)-1):
        n = w[i+1] - w[i]
        m = h[j+1] - h[j]
        result.append(n*m)

result_m = max(result)

print(result_m)



    