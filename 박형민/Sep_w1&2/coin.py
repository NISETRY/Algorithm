# [문제] 동전의 최소 개수
# 규칙: 큰 동전부터 나누자
coin_list = [100, 50, 500, 10]
target = 1730
cnt = 0
result = 0

# Greedy 문제의 단골 손님
# 정렬 연습: 튜플이라면? 인스턴스 리스트? 역순이라면?
#       예) 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬
# list.sort() vs sorted()
coin_list.sort(reverse=True)
print(coin_list)

for coin in coin_list:
    possible_cnt = target // coin
    result += possible_cnt
    target -= coin * possible_cnt
    # 현재 동전으로 가능한 최대 수
    # 정답에 더해준다
    # 금액을 빼준다

print(result)
