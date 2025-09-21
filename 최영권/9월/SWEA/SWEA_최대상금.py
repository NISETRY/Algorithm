from itertools import combinations
T = int(input())


def dfs(check_num, cnt):
    global answer
    if cnt == 0:
        answer = max(answer, check_num)
        return
    
    # 같은 카운트에 같은 값이 있으면 for문을 돌 필요가 없음
    if check_num in money_set:
        return
    
    # 없는 상금 add
    money_set.add(check_num)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            money_list[i], money_list[j] = money_list[j], money_list[i]
            dfs(int(''.join(money_list)), cnt - 1)
            money_list[i], money_list[j] = money_list[j], money_list[i]


for tc in range(1, T+1):
    nums, n = input().split()
    n = int(n)

    # 문자열은 불변이기 때문에 상금의 각 자리수에 해당하는 숫자를 리스트화
    money_list = []
    for num in nums:
        money_list.append(num)

    answer = 0

    money_set = set()
    dfs(int(''.join(money_list)), n)    

    print(f"#{tc} {answer}")