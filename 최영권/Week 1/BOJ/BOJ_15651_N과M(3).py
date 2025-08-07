N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

picked = []

def permute_repeat(count):
    if M == count:
        for picknum in picked:
            print(picknum, end = ' ')
        print()    
        return
    for num in numbers:
        picked.append(num)
        permute_repeat(count+1)
        picked.pop()

permute_repeat(0)