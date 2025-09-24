# 중복순열
numbers = [1,2,3,4,5] 
M = 2 
picked = [] 
def dupli_perm(cnt): 
    if cnt == M: 
        print(picked) 
        return 
    for i in range(len(numbers)):
        picked.append(numbers[i]) 
        dupli_perm(cnt+1)
        picked.pop() 
dupli_perm(0) 


# 순열
numbers = [1,2,3,4,5]
M = 2
picked = [] 
visited = [0] *len(numbers)
def perm(cnt):
    if cnt == M:
        print(picked) 
        return
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = 1 
            picked.append(numbers[i]) 
            perm(cnt+1) 
            visited[i] = 0 
            picked.pop() 
perm(0) 


numbers = [1,2,3,4,5] 
M = 2 
picked = [] 
def comb(cnt, idx): 
    if cnt == M: 
        print(picked) 
        return 
    for i in range(idx, len(numbers)): 
        picked.append(numbers[i]) 
        comb(cnt+1, i+1) 
        picked.pop() 
comb(0, 0) 


# 조합
numbers = [1,2,3,4,5] 
M = 2 
picked = [] 
def dupli_comb(cnt, idx): 
    if cnt == M: 
        print(picked) 
        return 
    for i in range(idx, len(numbers)):
        picked.append(numbers[i]) 
        dupli_comb(cnt+1, i) 
        picked.pop() 
dupli_comb(0, 0) 