def dfs(data, count):
    global result
    key = (''.join(data), count)
    if key in visited:
        return
    visited.add(key)

    if count == int(cnt):
        result = max(int(''.join(data)), result)
        return result

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            # if data[i] <= data[j]:
            data[i], data[j] = data[j], data[i]
            dfs(data, count+1)
            data[i], data[j] = data[j], data[i] # 다시 돌리기

T = int(input())

for tc in range(1, T+1):

    data, cnt = input().split()
    data = list(data)
    result = 0
    visited = set() # 나왔던 값 중복 저장 X
    dfs(data, 0)
    print(f'#{tc} {result}')


# 방문 처리 ( 나왔던 숫자 다시 안나오게 )
