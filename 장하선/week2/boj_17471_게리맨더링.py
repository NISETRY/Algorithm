n=int(input())
population=list(map(int,input().split()))
nearby=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    near=list(map(int,input().split()))
    for j in range(1,len(near)):
        nearby[i+1][near[j]]=nearby[near[j]][i+1]=1
for i in range(len(nearby)):
    print(nearby[i])
