N = 3 # 데이터의 개수
numbers = [1, 2, 3]

# 부분집합은 조합이랑 관련 깊음
# 데이터가 N개가 있다면, 3C0 + 3C1 + 3C2 + 3C3

# 모든 경우의 수 체크 - 2**N
visited = [0]*N

# 비선형
# 재귀로 짜는 것이 좋음

def subset(count):
    if count == N:
        # visited 결정
        # print(visited)
        for i in range(N):
            if visited[i]:
                print(numbers[i], end = ' ')
        print()
        return 

    # 선택하지 않은 것 : visited를 건드리지 않고 그대로 보냄
    subset(count+1)

    # 선택한 것
    visited[count] = 1
    subset(count+1)

    # 돌아오면 원복 시켜줘야함. 갈 떄 +1 해줬으니까
    visited[count] = 0

subset(0)
    