T = int(input())

for tc in range(1, T+1):
    sentence = input()
    pair = {'(':')','{':'}', '[':']'}

    stack = [0] * len(sentence)
    top = -2
    ans = 1
    for chr in sentence:
        if chr in pair.keys():
            top += 1
            stack[top+1] = chr
            # print("1", stack[:5])

        elif chr in pair.values():
                if pair.get(stack[top+1]) == chr:                       
                    # print("2", stack[:5])
                    stack[top+1] = 0
                    top -= 1
                else:   # 
                    ans = 0
                    break
                
    if stack[top+1] != 0:
        # print("3", stack[:5])
        ans = 0         
        
    print(f"#{tc} {ans}")

    