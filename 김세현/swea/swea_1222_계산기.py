# for tc in range(10):
#     N = int(input())
#     arr = list(map(int, input.split('+')))
#     arr_sum = sum(arr)
#     print(f'#{tc+1} {arr_sum}')

T = 10

for tc in range(T):
    N = int(input())
    arr = input()

    stack = []
    postfix = ''

    for ch in arr:
        if ch.isdigit(): 
            postfix += ch
        else:  
            while stack:
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()

    cal = []
    for ch in postfix:
        if ch.isdigit():
            cal.append(int(ch))
        else: 
            b = cal.pop()
            a = cal.pop()
            cal.append(a + b)

    print(f'#{tc+1} {cal[0]}')
