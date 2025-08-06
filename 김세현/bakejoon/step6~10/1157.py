word = input().upper()

word_list = []
for c in word:
    if c not in word_list:
        word_list.append(c)

result =[]

for i in word_list:
    count = word.count(i)

    result.append(count)


if result.count(max(result)) > 1:
    print("?")
else:
    print(word_list[result.index(max(result))])

