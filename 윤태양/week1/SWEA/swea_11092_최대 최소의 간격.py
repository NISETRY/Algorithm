t = int(input())
 
for i in range(t):
    l = int(input())
    num = list(map(int, input().split()))
    num2 = num[::-1]
    print(f'#{i+1} {abs(num.index(min(num))-(l-1-num2.index(max(num2))))}')