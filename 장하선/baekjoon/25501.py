def is_palinedrome(str):
    m=len(str)//2
    is_pal=1
    cnt=0
    if len(str)%2==1:
        cnt=1
        for i in range(1,m+1):
            cnt+=1
            if str[m-i]!=str[m+i]:
                is_pal=0
                break
    else:
        for i in range(m-1): #m-1=1, m=2
            cnt+=1
            if str[m-1-i]!=str[m+i]: # 1 2 / 0 3
                is_pal=0
                break
    return is_pal, cnt
cnt=0
def recursion(s, l, r):
    global cnt
    cnt+=1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n=int(input())
for _ in range(n):
    cnt=0
    s=input()
    print(isPalindrome(s), cnt)

