import sys
n = int(sys.stdin.readline())

queue = []
for i in range(n):
    
    raw = sys.stdin.readline().split()
    txt = raw[0]

    if "push" in raw:
        queue.append(raw[1])
        
    elif "pop" == txt:
        if queue:
       
            print(queue.pop(0))
        else:
            print(-1)

    elif "size" == txt:
        print(len(queue))


    elif "empty" == txt:
        if queue:
            print(0)
        else:
            print(1)

    elif "front" == txt:
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)