# 백준) 7단계. 2차원 배열 - 10798번. 세로 읽기

n = [list(input()) for _ in range (5)]

# print(n)

new = ''
for r in range(15): # 열 (각 줄에는 최소 1개, 최대 15개의 글자)
    for c in range(5): # 행
        
        # 현재 행(c)의 길이가 현재 r의 인덱스보다 크면 new 문자열에 저장
        # 해당 위치에 글자가 존재한다면
        if len(n[c]) > r:  
            new += n[c][r]


        # 인덱스가 없는 경우, 건너뛰기
        # if n[c][r] is False: -> 빈 배열이니깐 애초에 False 값인지 확인 못함
        #     continue
            # new += n[c][r]

print(new)


# 열을 읽어나갈 때, 글자가 없는 경우 때문에 
#     new += n[c][r]
#            ~~~~^^^
# IndexError: list index out of range