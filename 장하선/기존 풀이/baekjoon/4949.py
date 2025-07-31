while True:
    str=input()
    stack=[]
    if str=='.':
        break
    for x in str:
        if x=='(' or x=='[':
            stack.append(x)
        elif x==')':    
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(x)
                break
        elif x==']':
            if len(stack)>0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(x)
                break
    if len(stack)==0:
        print('yes')
    else:
        print('no')