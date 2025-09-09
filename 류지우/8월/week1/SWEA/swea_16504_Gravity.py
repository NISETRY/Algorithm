T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 가로 N
    arr = list(map(int, input().split()))

    distance_num = []
    for i in range(N):
        distance = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                distance += 1
        distance_num.append(distance)

    # print(result)
    answer = max(distance_num)
    print(f'#{tc} {answer}')


# 모든 수의 낙차의 값을 저장하지 않고, 가장 큰 낙차의 값만 저장
T = int(input())

for tc in range(1, 1+T):
    N = int(input()) # 가로 N
    arr = list(map(int, input().split()))

    distance_num = 0
    for i in range(N):
        distance = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                distance += 1
        if distance_num < distance: 
            distance_num = distance

    print(f'#{tc} {distance_num}')


# 강사님 아이디어
# 상태 공간이 비지 않게 끔 - 나올 수 있는 경우의 수를 모두 고려하자.
# 오른쪽에 있는 블록의 수 
# 가로 길이 수 - 현재보다 오른쪽에 있는 블록의 수 = 낙차
# 가로 길이 - 1 - 블록 수 = 낙차
# 오른쪽의 블록 수만 변경됨. 

# 오른쪽에 있는 블록이 왼쪽 블록보다 같거나 작으면 굳이 돌지 않아도 되지 않나?
# 오른쪽에 있는 블록보다 왼쪽 블록이 클 때만 검사할거임


T = int(input())

for tc in range(1, 1+T):
    width = int(input())
    heights = list(map(int, input().split()))
    answer = 0
    max_heihgt = 0

    for i in range(width):
        if heights[0] <= max_heihgt:
            continue

        max_heihgt = heights[i]
        lower_count = 0
        for j in range(i+1, width):
            if heights[i] > heights[j]:
                lower_count += 1
        
        answer = max(answer, lower_count)
        # 위의 한 줄과 같은 코드
        #   if distance_num < distance: 
        #    distance_num = distance
