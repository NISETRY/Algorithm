import sys
N = int(sys.stdin.readline().rstrip())
lst = [0] * N
for i in range(N):
    lst[i] += int(sys.stdin.readline().rstrip()) 


for num in sorted(lst):
    print(num)
