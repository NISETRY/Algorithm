import sys
n = int(sys.stdin.readline())

deque = []
for i in range(n):
    
    raw = sys.stdin.readline().split()
    txt = raw[0]

    if "push_front" in raw:
        if deque:
            deque = deque + [0]
            for i in range(len(deque)-1,0,-1):
                deque[i] = deque[i-1]
            deque[0] = raw[1]
            
        else:
           deque.append(raw[1])

    elif "push_back" in raw:
        deque.append(raw[1])
    

    elif "pop_front" == txt:
        if deque:
       
            print(deque.pop(0))
        else:
            print(-1)

    elif "pop_back" == txt:
        if deque:
       
            print(deque.pop(-1))
        else:
            print(-1)

    elif "size" == txt:
        print(len(deque))


    elif "empty" == txt:
        if deque:
            print(0)
        else:
            print(1)

    elif "front" == txt:
        if deque:
            print(deque[0])
        else:
            print(-1)
    else:
        if deque:
            print(deque[-1])
        else:
            print(-1)