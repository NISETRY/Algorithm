i=input
for t in range(1,int(i())+1):
    a,b=i(),i()
    print(f'#{t} {max(b.count(c) for c in a)}')