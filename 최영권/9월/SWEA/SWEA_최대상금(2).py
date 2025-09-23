T = int(input())

def dfs(chr, cnt):
    global max_prize

    if change == 0:
        max_prize = max(max_prize, chr)
        return
    if chr in money_set:
        return 
    money_set.add(chr)
    for i in range(len(money_lst)):
        for j in range(i+1, len(money_lst)):
            money_lst[i], money_lst[j] = money_lst[j], money_lst[i]
            dfs(int(''.join(money_lst)), cnt - 1)
            money_lst[i], money_lst[j] = money_lst[j], money_lst[i]



for tc in range(1, T+1):
    money, change = input().split()
    change = int(change)
    money_lst = list(money)
    money_set = set()
    max_prize = 0
    dfs(int(''.join(money_lst)), change)
    
    
    print(f"#{tc} {max_prize}") 