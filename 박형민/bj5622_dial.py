alp = [chr(i) for i in range(65,91)]
# 이렇게 만든 알파벳을 2부터 3개씩,
# 조건문으로 7과 9는 4개씩 넣는다.

'''
딕셔너리에서 key 값은 중복이 안되지만, value는 중복 가능
알파벳 3개씩을 key로, value에는 같은 숫자 2를, 이런식으로 반복
value 가 7, 9 일때에는 예외처리
챗지피티한테 물어봤는데 다이얼 만드는 건
어떻게 알고 알아서 아래 반복문 코드를 다 짜줘서 참고했습니다.
'''
dial_dict = {}


idx = 0 # 알파벳 인덱스 용 빈 변수
num = 2
for i in range(2, 10):
    if i in [7, 9]:
        step = 4
    else:
        step = 3
    for j in alp[idx : idx + step]:
        dial_dict[j] = i
    idx += step

word = list(input())
answer = 0

for i in word:
    answer += dial_dict[i] + 1
print(answer)

'''
special thanks to:
chat GPT
{'a': 2, 'b': 2, 'c': 2
 ,'d': 3, 'e': 3, 'f': 3
 ,'g': 4, 'h': 4, 'i': 4}
이렇게 딕셔너리 짜는 코드 만들어줌
'''