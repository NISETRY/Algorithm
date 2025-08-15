t = int(input())
 
for tc in range(t):
    str1 = list(input())
    str2 = list(input())
    idx = [0]*26
 
    for i in str2:
        if i in str1:
            idx[ord(i)-ord('A')] += 1  # ord 사용으로 글자 인덱스 가져옴 
                                       # 만약 대소문자가 같이 왔다면 upper/lower 후에 똑같이 하면 될 듯
    print(f'#{tc+1} {max(idx)}')