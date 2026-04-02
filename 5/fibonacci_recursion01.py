def fibonacchi(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacchi(n - 1) + fibonacchi(n - 2)
    
print("fibonacchi(1): ", fibonacchi(1))
print("fibonacchi(2): ", fibonacchi(2))
print("fibonacchi(3): ", fibonacchi(3))
print("fibonacchi(4): ", fibonacchi(4))
print("fibonacchi(5): ", fibonacchi(5))