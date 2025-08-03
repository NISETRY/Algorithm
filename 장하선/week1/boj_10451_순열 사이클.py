T=int(input())
for t in range(T):
    n=int(input())
    nums=[-1] # 인덱스 맞췆주기 위해 0번 인덱스에 값 할당, 이후 반복문에서 순열 사이클에 걸리지 않기 위해 -1 넣음
    k=list(map(int, input().split()))
    nums.extend(k) # 인덱스 맞춘거에 입력받은 수열 붙이기
    sn=1 # 1번부터 순회 시작
    res=[[] for _ in range(n)] # 최대 n개의 순열 사이클이 있을 것이기에 n개의 내부행렬 만들어줌
    x=0 # res에 저장될 순열 사이클의 index
    cnt=0 # res에서 길이가 1 이상인 것을 카운팅. 최종 정답
    while True:
        if len(k)==0: # 수열 다 돌면 탈출
            break
        if sn not in res[x]:
            res[x].append(sn)
            sn=nums[sn]
            k.remove(sn) # 한 번 본 수는 더 이상 안보기 위해서
        else:
            x+=1 # 순열 사이클 하나 완료하면 다음 순번에 채우기
            sn=min(k) # 하나의 사이클이 채워지면 다음 수 후보는 제일 작은거부터
    for i in res:
        if len(i)!=0:
            cnt+=1
        else: # 길이가 0인게 나오면 뒤에 나오는거도 다 길이 0이니까 break. 더 볼 필요 없음
            break
    print(cnt)