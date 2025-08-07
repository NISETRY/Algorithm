for t in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
 
    for i in range(dump):
        box[box.index(max(box))] = max(box) - 1
        box[box.index(min(box))] = min(box) + 1
 
    print(f'#{t+1} {max(box)-min(box)}')