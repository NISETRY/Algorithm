T = int(input())


def binary_search(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = (start+end)//2
        count += 1
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle 
    return count



for tc in range(1, T+1):
    total, page_A, page_B = map(int, input().split())

    search_A = binary_search(total, page_A)
    search_B = binary_search(total, page_B)

    print(search_A, search_B)
    if search_A < search_B:
        print(f"#{tc} A")
    elif search_A == search_B:
        print(f"#{tc} 0")
    elif search_A > search_B:
        print(f"#{tc} B")