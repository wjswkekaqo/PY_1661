counter = 0

def fibonacchi(n):
    print("fibonacchi({})를 구합니다.".format(n))
    global counter
    counter += 1
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacchi(n - 1) + fibonacchi(n - 2)

fibonacchi(50)
print("---")
print("fibonacchi(10) 계산할 때 함수를 호출한 횟수는 {}번입니다.".format(counter))