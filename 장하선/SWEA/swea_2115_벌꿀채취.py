def select(honey, idx, tot, pro):
    if tot>c:
        return 0
    if idx==m:
        return pro
    sel=select(honey, idx+1, tot+honey[idx], pro+honey[idx]**2)
    non=select(honey, idx+1, tot, pro)
    return max(sel, non)

def chaemil(honey):
    if sum(honey)<=c:
        return sum(i**2 for i in honey)
    return select(honey,0,0,0)

T=int(input())
for tc in range(1,T+1):
    n,m,c=map(int, input().split())
    honeycomb=[list(map(int,input().split())) for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    for a in range(m):
        visited[0][a]=True
    max_profit=0
    for i in range(n):
        for j in range(n-m+1):
            honey_1=honeycomb[i][j:j+m]
            visited[i][j+m-1]=True
            profit_1=chaemil(honey_1)
            for x in range(n):
                for y in range(n-m+1):
                    honey_2=honeycomb[x][y:y+m]
                    # [x][y:y+m]의 원소 중 1개라도 visited=True면 아래 연산 안함
                    if True not in visited[x][y:y+m]:
                        profit_2=chaemil(honey_2)
                        total=profit_1+profit_2
                        max_profit=max(max_profit, total)
                        # print(profit_1,profit_2)
    print(f'#{tc} {max_profit}')

# def chaemil(honey):
#     honey.sort()
#     bee_1,pro_1=0,0
#     bee_2,pro_2=0,0
#     if sum(honey)<=c:
#         return sum(i**2 for i in honey)
#     for i in range(len(honey)):
#         bee_1+=honey[i]
#         if bee_1<=c:
#             pro_1+=honey[i]**2
#     for i in range(len(honey)-1,-1,-1):
#         bee_2+=honey[i]
#         if bee_2<=c:
#             pro_2+=honey[i]**2
#     return max(pro_1, pro_2)
# T=int(input())
# for tc in range(1,T+1):
#     n,m,c=map(int, input().split())
#     honeycomb=[list(map(int,input().split())) for _ in range(n)]
#     visited=[[False]*n for _ in range(n)]
#     for a in range(m):
#         visited[0][a]=True
#     max_profit=0
#     for i in range(n):
#         for j in range(n-m+1):
#             honey_1=honeycomb[i][j:j+m]
#             visited[i][j+m-1]=True
#             profit_1=chaemil(honey_1)
#             for x in range(n):
#                 for y in range(n-m+1):
#                     honey_2=honeycomb[x][y:y+m]
#                     # [x][y:y+m]의 원소 중 1개라도 visited=True면 아래 연산 안함
#                     if True not in visited[x][y:y+m]:
#                         profit_2=chaemil(honey_2)
#                         total=profit_1+profit_2
#                         max_profit=max(max_profit, total)
#                         # print(profit_1,profit_2)
#     print(f'#{tc} {max_profit}')