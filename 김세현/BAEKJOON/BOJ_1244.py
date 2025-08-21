N = int(input())
stat = list(map(int, input().split()))
num_student = int(input())

for _ in range(num_student):
    a, b = map(int, input().split())

    # 남학생
    if a == 1:
        for id in range(b-1, N, b):
            stat[id] = 1 - stat[id]

    # 여학생
    elif a == 2:
        b -= 1
        stat[b] = 1 - stat[b]
        d = 1
        while b - d >= 0 and b + d < N and stat[b - d] == stat[b + d]:
                stat[b - d] = 1 - stat[b - d]
                stat[b + d] = 1 - stat[b + d]
                d += 1

for i in range(N):
    print(stat[i], end=' ')
    if (i+1) % 20 == 0:
        print()
