dictionary = {
    1: 1,
    2: 1
}

def fibonacchi(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacchi(n - 1) + fibonacchi(n - 2)
        dictionary[n] = output
        return output

print("fibonacchi(10): ", fibonacchi(10))
print("fibonacchi(20): ", fibonacchi(20))
print("fibonacchi(30): ", fibonacchi(30))
print("fibonacchi(40): ", fibonacchi(40))
print("fibonacchi(50): ", fibonacchi(50))