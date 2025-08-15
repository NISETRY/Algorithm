arr=list(map(int,input().split()))

# 버블 정렬
def bubble_sort(arr):
    l=len(arr)
    for i in range(l):
        for j in range(1,l):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

# 선택 정렬
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 카운팅 정렬
def counting_sort(arr):
    if not arr:
        return []
    temp=[0]*len(arr)
    cnt=[0]*(max(arr)+1)
    for i in arr:
        cnt[i]+=1
    for i in range(max(arr)):
        cnt[i+1]+=cnt[i]
    for i in range(len(arr)-1,-1,-1):
        cnt[arr[i]]-=1
        temp[cnt[arr[i]]]=arr[i]
    return temp

# 순열 : 재귀와 visited를 활용한 함수
permutation_num=list(map(int, input().split()))
m=int(input())
pick=[]
cnt=0
visited=[0]*(len(permutation_num)+1)
def nPm(count,m):
    global cnt
    if count==m:
        cnt+=1
        print(*pick)
        return
    for i in permutation_num:
        if visited[i]==1:
            continue
        pick.append(i)
        visited[i]=1
        nPm(count+1,m)
        pick.pop()
        visited[i]=0
nPm(0,m)
print(cnt)

# 순차 검색
def sequential_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


# 이진정렬
def binary_sort(arr, target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return target
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return -1