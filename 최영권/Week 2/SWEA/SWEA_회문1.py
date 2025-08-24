# T = 10
# for tc in range(1, T+1):
#     length = int(input())

#     lst = [list(input()) for _ in range(8)]
#     count = 0

#     # 가로
#     for row in lst:
#         for col in zip(*row):

#             for i in range(8-length+1):
#                 string = row[i:i+length]
#                 if string == string[::-1]:
#                     count += 1

#     for col in zip(*lst):
#         for j in range(8-length+1):
#             string = col[j:j+length]
#             if string == string[::-1]:
#                 count += 1
    
#     print(f"#{tc} {count}")
    

# 강사님 코드
T = 10
for tc in range(1, T+1):
    N = int(input())

    graph = [input() for _ in range(8)]  # 수정을 위해서 리스트로 받아오는건데 이 문제는 참조만 진행하니까 굳이 리스트로 받을 필요 없음
    answer = 0

    # 가로
    for i in range(8):
        for j in range(8-N+1):
            
            # 행검사
            for k in range(N//2):
                if graph[i][j+k] != graph[i][j+N-1-k]:
                    break
            else:
                answer += 1

            # 열검사
            for k in range(N//2):
                if graph[j+k][i] != graph[j+N-1-k][i]:
                    break
            else:
                answer += 1


    print(f"#{tc} {answer}")
    