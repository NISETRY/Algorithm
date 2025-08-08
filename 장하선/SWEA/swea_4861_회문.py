T=int(input())
# 세로 회문 확인을 위한 전치행렬 함수 구현
def transpose(matrix):
    trans=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            trans[j][i]=matrix[i][j]
    return trans

for tc in range(1,T+1):
    # 입력 받기
    n,m=map(int,input().split())
    palindrome=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        string=input()
        for j in range(n):
            palindrome[i][j]=string[j]

    # 가로 회문 확인
        palin=False # flag 설정
        for j in range(n-m+1): # 길이 m인 회문이니까 반복 횟수 겸 시작할 인덱스 설정
            for x in range(m//2):
                if palindrome[i][x+j]!=palindrome[i][m-1-x+j]:
                    break
            if x==m//2-1:
                pal=''
                for y in range(m):
                    pal+=palindrome[i][j+y]

    # 세로 회문 확인
    if not palin: # 가로 회문 있으면 볼 필요 없음
        palindrome=transpose(palindrome) # 전치행렬로 변환
        for i in range(n):                                                                                                                                                                                                                                                                                                                                                                                                                                                       
            for j in range(n-m+1): # 길이 m인 회문이니까 반복 횟수 겸 시작할 인덱스 설정
                for x in range(m//2):
                    if palindrome[i][x+j]!=palindrome[i][m-1-x+j]:
                        break
                if x==m//2-1:
                    pal=''
                    for y in range(m):
                        pal+=palindrome[i][j+y]
    print(f'#{tc} {pal}')