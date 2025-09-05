# 버블 정렬

def bubble_sort(a,N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j]> a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubble_sort1(a,N): # 정렬할 list, N 원소의 수
    for i in range(N-1): # 확정시키고 싶은 숫자의 수
        for j in range(N-1-i): # 비교 연산이 몇 번 필요한지
            if a[j] > a[j+1]: # 오름차순, 내림차순은 <
                a[j], a[j+1] = a[j+1], a[j]


a = [1, 8, 3, 4, 7, 2]
b = [1, 8, 3, 4, 7, 2, 5]
print(a)
bubble_sort1(a,6)
print(a)



