n=int(input())
if n==4 or n==7:
    print(-1)
elif n%5==1 or n%5==3: #6 -1 +2 #3 0 +1
    print(n//5+1)
elif n%5==2 or n%5==4: #9 -1 +3 #12 -2 +4
    print(n//5+2)
else: #0
    print(n//5)