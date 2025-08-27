def comb(count, idx):
    if count == l:
        pick.append(temp[:])
        return
    
    for i in range(1, c+1):
        if i>idx:
            temp.append(words[i])
            comb(count+1, i)
            temp.pop()

l, c = map(int, input().split())
words = list(input().split())
words = [0] + sorted(words)
temp = []
pick = []

comb(0,0)

for i in pick:
    check_ja, check_mo = 0, False
    word = ''
    for j in i:
        if j in ['a','e','i','o','u']:
            check_mo = True
            word += j
            continue
        else:
            check_ja += 1
            word += j

    if check_ja >=2 and check_mo == True:
        print(word)

