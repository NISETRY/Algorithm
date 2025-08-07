T = int(input())

def binarySearch(P, key):
        start = 1
        end = P
        count = 0

        while start <= end :
            count += 1
            middle = (start + end)//2
            if middle == key :
                return count
            elif middle > key :
                end = middle 
            else :
                start = middle
        return count


for tc in range(T):

    P, Pa, Pb = map(int, input().split())

    count_A = binarySearch(P, Pa)
    count_B = binarySearch(P, Pb)


    if count_A < count_B:
        answer = 'A'
    elif count_A > count_B:
        answer = 'B'
    else:
        answer = '0'

    print(f'#{tc+1} {answer}')
