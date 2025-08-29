def cal(node):
    # 자식 노드가 없으면 더 내려갈 수 없으니 값을 바로 반환
    if left[node]==0: return tree[node]
    x,y=cal(left[node]),cal(right[node])
    operator=tree[node]
    if operator=='+': return x+y
    if operator=='-': return x-y
    if operator=='*': return x*y
    if operator=='/': return x/y
for tc in range(1,11):
    n=int(input())
    # 노드를 입력받을 리스트
    tree=[0]*(n+1)
    # 자식 노드의 유무 확인, 0이면 해당 방향의 자식 노드가 없다는 것
    left=[0]*(n+1)
    right=[0]*(n+1)
    # 입력 받고, 수정하기
    for x in range(1,n+1):
        info=input().split()
        # 입력값 편집
        for i in range(len(info)):
            if info[i] not in '+-*/':
                info[i]=float(info[i])
        tree[x]=info[1]
        # 자식노드가 존재하는 경우
        if len(info)==3:
            left[x]=int(info[2])
        if len(info)==4:
            left[x]=int(info[2])
            right[x]=int(info[3])
    
    print(f'#{tc} {int(cal(1))}')