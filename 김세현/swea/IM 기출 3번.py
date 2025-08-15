di = [0,1,-1,0]
dj = [1,0, 0 ,-1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_count = 1
    for i in range(N):
        for j in range(N):
            x, y = i , j
            count = 1

            min_value = 9999999999999999

            while True :
                is_move = False

                next_x = -1
                next_y = -1
                for d in range(4):
                    ni = x + di[d]
                    nj = y + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < arr[x][y] and arr[ni][nj] < min_value:
                        min_value = arr[ni][nj]
                        next_x , next_y = ni , nj
                        is_move = True
                            
                if is_move:
                    x = next_x
                    y = next_y
                    count +=1
                else: 
                    break

            if max_count < count:
                max_count = count
          
    print(f'#{t+1} {max_count}')

                   


        

      
     





