# 재귀 기반 부분집합

def subs(i, N):

    if i == N:
        print(bit, end = ' | ')
        lst = []
        for j in range(N):
            if bit[j]:
                lst.append(arr[j])
        print(lst)
        return
    
    else:
        bit[i] = 0
        subs(i + 1, N)
        bit[i] = 1
        subs(i + 1, N)
        return

arr = [1, 2, 3]
bit = [0] * 3
subs(0, 3)

'''
참고: https://minmyeong2612.tistory.com/10
'''