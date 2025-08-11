t = int(input())
 
for tc in range(t):
    case = list(input())
    ans = 0
    pipe = 0
    stack = []
    razer_time = False
    for i in range(len(case)):                   # 레이저 타임인 경우, T/F 전환만 하고 컨티뉴
        if razer_time == True:
            razer_time = False
            continue
        if case[i] == "(" and case[i+1] == ")":  # 레이저인 경우, 무조건 다음은 스킵해야함
            ans+=pipe                            # ANS추가는 파이프 수 x 레이저
            razer_time = True
            continue
        elif case[i] == "(" and case[i+1] == "(": # 파이프가 추가되는 경우
            stack.append("1")
            pipe+=1
            ans+=1
        elif case[i] == ")":
            try:
                stack.pop(0)                      # 파이프가 빠지는 경우 (최적화 가능할 듯)
                pipe-=1
            except:
                pass
     
    print(f'#{tc+1} {ans}')