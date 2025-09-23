idx = int(input())

temp = []
picked = []

def comb():
    picked.append(temp[:])
    if len(picked) == 1000000:
        return

    for i in range(0, 10):
        if temp:
            if i < temp[-1]:
                temp.append(i)
                comb()
                temp.pop()

        else:
            temp.append(i)
            comb()
            temp.pop()

comb()
for_str = ''
answer = []

for i in range(len(picked)):
    now = picked[i]
    
    for i in now:
        for_str += str(i)

    if for_str:
        answer.append(int(for_str))
        for_str = ''

answer.sort()

try:
    print(answer[idx])

except:
    print(-1)