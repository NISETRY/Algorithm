n=int(input())
for i in range(n):
    s=str(i)
    dig=0
    for j in range(len(s)):
        dig+=int(s[j])
    if n==i+dig:
        print(i)
        break
if i==n-1:
    print(0)