n,m=map(int, input().split())
board=[]
refill=64
for i in range(n):
    k=input().strip()
    board.append([c=='B' for c in k])
for i in range(n-7):
    for j in range(m-7):
        blk,wht=0,0
        for x in range(8):
            for y in range(8):
                chess=board[x+i][y+j]
                if (x+y)%2==0:
                    if not chess:
                        blk+=1
                    else:
                        wht+=1
                else:
                    if chess:
                        blk+=1
                    else:
                        wht+=1
        refill=min(refill,blk,wht)
print(refill)