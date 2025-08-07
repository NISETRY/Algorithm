# 순열 재귀 구현
# 내가 뭘 골랐든 탐색 범위의 변화에 영향을 미치지지 않는다. 범위 안바뀜
numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3
visited = [0]*len(numbers)

def perm(count):
    if count == M:
        print(picked_numbers)
        return
    
    for i in range(len(numbers)):
        if visited[i] == 1:
            continue
        picked_numbers.append(numbers[i])
        visited[i] = 1
        perm(count+1)
        picked_numbers.pop()
        visited[i] = 0

perm(0)
    



# 순열 코드를 수정해서 조합으로 변경할 것
# 조합은 내가 뭘 골랐는지에 따라서 다음 탐색 범위가 변경됨.
# 내가 고른 거 빼고 탐색
# => 방문체크할 필요가 없음

numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3

def comb(count, idx):    # 내가 고른 idx가 필요함
    if count == M:
        print(picked_numbers)
        return
    
    for i in range(idx, len(numbers)): # 내가 고른 idx부터 검색해봐
        picked_numbers.append(numbers[i])
        comb(count+1, i+1)    # 
        picked_numbers.pop()


comb(0,0)
    

numbers = [1, 2, 3, 4, 5]
picked_numbers = []

def comb(count, idx):    # 내가 고른 idx가 필요함
    print(picked_numbers)
    if count == len(numbers):
        return
    
    for i in range(idx, len(numbers)): # 내가 고른 idx부터 검색해봐
        picked_numbers.append(numbers[i])
        comb(count+1, i+1)    # 
        picked_numbers.pop()


comb(0,0)
        