n=int(input())
start,k=665,0
while True:
    start+=1
    if '666' in str(start):
        k+=1
    if n==k:
        break
print(start)