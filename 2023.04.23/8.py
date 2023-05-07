while True:
    n = int(input())
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-2] + fib[-1])
    print(*fib)
    
# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 8.py
# 1
# 1 1
# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597