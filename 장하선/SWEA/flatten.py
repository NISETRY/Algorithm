for tc in range(1,11):
    dump=int(input())
    box=list(map(int, input().split()))
    max_idx=box.index(max(box))
    min_idx=box.index(min(box))
    while dump>0:
        dump-=1
        box[max_idx]-=1
        box[min_idx]+=1
        max_idx=box.index(max(box))
        min_idx=box.index(min(box))
        if sum(box)%10==0:
            if max(box)==min(box):
                break
        else:
            if max(box)-min(box)==1:
                break
    print(f'#{tc} {max(box)-min(box)}')