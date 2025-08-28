# 재귀 기반 순열

def per(i, N):

    if i == N:
        print(arr)
        return

    else:
        for j in range(i, N):       # 인덱스 0 기준 자리 바꾸기부터 시작
            arr[i], arr[j] = arr[j], arr[i]
            per(i + 1, N)                 # ij = 00 , 01, 02 일때 함수 호출
            arr[i], arr[j] = arr[j], arr[i]    # arr는 고정되어야 하기 때문에 제자리
        return

arr = [1, 2, 3]
per(0, 3)
N = 3


'''
참고: https://minmyeong2612.tistory.com/10
'''