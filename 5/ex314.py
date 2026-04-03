a = 2
b = 10
c = 100
memo = {}
def exam(d, f):
    key = str([d, f])
    
    if key in memo:
        return memo[key]
    if d < 0:
        return 0   
    if d == 0:
        return 1
    count = 0
    for i in range(f, b + 1):
        count += exam(d - i, i)        
    memo[key] = count
    return count

print(exam(c, a))