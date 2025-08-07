for _ in range(10):
    n = int(input())
    b = list(map(int,input().split()))
    jomang = 0
 
    for i in range(2, n-2):
        max_area = max([b[i-2],b[i-1],b[i+1],b[i+2]])    
        if b[i] - max_area >0:
            jomang+=b[i] - max_area
         
    print(f'#{_+1} {jomang}')