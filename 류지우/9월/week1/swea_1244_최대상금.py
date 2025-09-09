# SWEA 1244번 최대 상금

# 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여 받음
# 우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로 자리를 위치를 교환할 수 있다
# 정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
# 숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다

# 큰 수가 왼쪽에 위치해야 큰 상금을 받을 수 있음
# 횟수만큼 교환이 이루어져야 함
# 동일한 위치의 교환이 중복되어도 됨

# 정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산

def dfs(count):
    if count == N:
        return

    for current in range(len(nums)):
        for next in range(current+1, len(nums)):

            if nums[current] <= nums
    pass


T = int(input())

for tc in range(1, T+1):
    nums, N = input().split()
    N = int(N)
    nums = list(nums)

    dfs(0)


    for i in range(N):
        max_num = max(num)


    print(f'#{tc}')
