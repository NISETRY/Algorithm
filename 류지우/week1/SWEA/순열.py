numbers = [1, 2, 3, 4, 5]
pick_numbers = [] # 숫자를 뽑을 때마다 넣어줄 것
M = 3


# 중복순열
def perm(count):
	# 종료조건 : 내가 뽑은 수(count)가 M개가 되었을 때 종료
    if count == M:
        print(pick_numbers)
        return

    # 숫자를 하나 뽑기. 
    for i in range(len(numbers)):
        pick_numbers.append(numbers[i])
        perm(count+1)
        pick_numbers.pop()

# 아무것도 안골랐음
perm(0)



# 중복순열X - visited를 체크할것? 방문여부를 변경하는것. 방문하면 1로 변경

# numbers의 값을 뽑았는지 안뽑았는지 알고 싶어
visited = [0]*len(numbers)

def perm2(count):
	# 종료조건 : 내가 뽑은 수(count)가 M개가 되었을 때 종료
    if count == M:
        print(pick_numbers)
        return

    # 숫자를 하나 뽑기. 
    for i in range(len(numbers)):
        if visited[i] != 1:
            pick_numbers.append(numbers[i])
            visited[i] = 1
            perm(count+1)
            pick_numbers.pop()
            visited[i] = 0

    # # 숫자를 하나 뽑기. 
    # for i in range(len(numbers)):
    #     if visited[i] == 1:
    #         continue
    #     pick_numbers.append(numbers[i])
    #     visited[i] = 1
    #     perm(count+1)
    #     pick_numbers.pop()
    #     visited[i] = 0


# 아무것도 안골랐음
perm2(0)