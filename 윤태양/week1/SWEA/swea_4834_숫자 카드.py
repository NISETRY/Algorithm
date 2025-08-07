t = int(input())
 
for k in range(t):
    l = int(input())
    card = list(map(int, input()))
     
    ans = [0]*(10)
 
    for i in card:
        ans[i] += 1
 
    ans = ans[::-1]
    idx = ans.index(max(ans))
 
    print(f'#{k+1} {10-idx-1} {max(ans)} ')