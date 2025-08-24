def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fibonacchi(n-1) + fibonacchi(n-2)
    
print(fibonacchi(int(input())))
    