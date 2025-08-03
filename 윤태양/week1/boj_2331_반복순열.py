# 푸는 중

a, p = map(int, input().split())
n = [a]
b = 1

while b==1:
    num = 0
    
    for i in str(a):
        num += int(i)**p
        if num in n:
            b=0

    n.append(num)
    a = num

qq = n.index(num)
print(len(n[:qq]))