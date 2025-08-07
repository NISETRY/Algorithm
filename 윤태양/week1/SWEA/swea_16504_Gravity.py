n = int(input())
 
for i in range(n):
    input()
    b = list(map(int, input().split()))
    ans = []
     
    for j in range(len(b)):
        ans1 = 0
        for k in range(j+1, len(b)):
            if b[j] > b[k]:
                ans1+=1
        ans.append(ans1)
     
    print(f'#{i+1} {max(ans)}')