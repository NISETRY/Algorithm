from collections import deque

T = 10 
for tc in range(1, T+1):
    input()
    nums = deque(map(int, input().split()))
    minus = list(range(1,6))
    
    d = 0
    while nums[-1] > 0:
        left = nums.popleft() - minus[d % 5]
        if left < 0:
            left = 0
        nums.append(left)
        d += 1
    
    print(f"#{tc} ", *nums)