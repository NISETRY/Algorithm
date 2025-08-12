T=int(input())
for tc in range(1,T+1):
    str1=input()
    str2=input()
    max_count=0
    for x in str1:
        val=0
        for y in str2:
            if x==y:
                val+=1
        max_count=max(max_count,val)
    print(f"#{tc} {max_count}")