N, M = map(int, input().split())

num = list(map(int, input().split()))

result = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            if num[i]+num[j]+num[k] <= M:
                result.append(num[i]+num[j]+num[k])


print(max(result))
