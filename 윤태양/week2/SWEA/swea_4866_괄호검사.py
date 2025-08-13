t = int(input())
for tc in range(t):
    l = list(input())
    stack = []
    ans = 1
    for i in l:
        if i == '{': 
            stack.append(i)
        elif i == '(':
            stack.append(i)

        elif i == '}':  ## pop 연산은 트라이로 함
            try:
                b = stack.pop()
                if b!= '{':
                    ans=0
            except:
                ans = 0
        
        elif i == ')':
            try:
                b = stack.pop()
                if b!= '(':
                    ans=0
            except:
                ans = 0
                
    if len(stack)>=1:
        ans  = 0
    print(f'#{tc+1} {ans}')
