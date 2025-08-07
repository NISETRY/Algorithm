N = int(input())

cnt = N

for _ in range(N):

    word = input()

    if len(word) == 1: #문자열이 1개이면 그룹 단어
        cnt += 0

    else:
        for i in range(len(word)-1):
            if word[i] == word[i+1]: # 바로 뒤 문자와 비교하여 같으면 pass
                pass

            elif word[i] in word[i+1:]: # 바로 뒤 문자와 다른 경우, 뒤에 나오는 문자열에 해당 문자가 있으면 -1 하고 끝냄
                cnt -= 1
                break
            

print(cnt)