T=int(input())
for tc in range(1,T+1):
    string=input()
    stack=[]
    ans=1
    for x in range(len(string)):
        if string[x]=='{' or string[x]=='(':
            stack.append(string[x])

        elif string[x]=='}':
            if len(stack)==0:
                ans=0
                break
            if stack[-1]=='{':
                stack.pop()
            elif stack[-1]=='(':
                ans=0
                break

        elif string[x]==')':
            if len(stack)==0:
                ans=0
                break
            if stack[-1]=='(':
                stack.pop()
            elif stack[-1]=='{':
                ans=0
                break
            
    if len(stack)!=0:
        ans=0
    print(f'#{tc} {ans}')