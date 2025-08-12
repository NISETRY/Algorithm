def check(inputValue):
    matching_dict = {'}':'{', ')':'('}
    stack = []
    for i in inputValue:
        if i in ('{','('):
            stack.append(i)
        elif i in ('}',')'):
            if not stack or stack[-1] != matching_dict[i]:
                return 0
            stack.pop()

    if stack:
        return 0
    else:
        return 1
    
T = int(input())
for tc in range(T):
    print(f'#{tc+1} {check(input())}')