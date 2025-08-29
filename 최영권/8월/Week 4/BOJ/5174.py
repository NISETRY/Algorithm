# 순회 -> visit (T) cnt += 1
def pre_order(T):
    global cnt
    if T > 0:
        cnt += 1            
        pre_order(left[T])    # pre_order(T.left)
        pre_order(right[T]) 

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1 # 마지막 정점번호
    left = [0] * (V+1)
    right = [0] * (V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]     
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0 
    pre_order(N)
    print(f"#{tc} {cnt}")