'''
3           T(tc수)

5 1         N(돌의 수), M(뒤집기 횟수)
0 1 0 1 0   초기상태
2 2         i(i번째 돌), j(마주보는 j개 돌)

5 1         N, M
0 1 0 0 0   초기
2 3         i, j

10 4        N, M
0 1 1 0 0 1 0 1 0 1 초기
3 2         i, j    M(뒤집기 횟수 만큼)
5 3         i, j
4 4         i, j
8 4         i, j
'''

T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    default = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        for l in range(1, j + 1):
            if 0 <= i-1 - l and i-1 + l <= N - 1:
                if default[i-1 - l] == default[i-1 + l]:
                    default[i-1 - l] = 1 - default[i-1 - l]
                    default[i-1 + l] = 1 - default[i-1 + l]
    
    print(f'#{tc}',*default)

####################################################################

    N,M = map(int,input().split())
    stones = list(map(int,input().split()))
    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1 # 인덱스를 0으로 맞추기
 
        left = i - 1
        right = i + 1
 
        for _ in range(j):
            if 0 <= left and right < N and stones[left] == stones[right]:
                stones[left] = 1 - stones[left] # 돌 뒤집기
                stones[right] = 1 - stones[right] # 돌 뒤집기
            left -= 1
            right += 1
    print(f'#{tc}', *stones)