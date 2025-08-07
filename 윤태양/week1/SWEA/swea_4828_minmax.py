# input()
n = int(input())
 
for a in range(n):
    input()
    l = list(map(int, input().split()))
    max = -1
    min = 100000000000
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
        if l[i] < min:
            min = l[i]
 
    print(f'#{a+1} {max-min}')