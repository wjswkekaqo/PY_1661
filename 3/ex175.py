a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

if a > b:
    print("처음 입력했던 {} 가  {}보다 큽니다.".format(a, b))
if a < b:
    print("두 번째 입력했던 {} 가  {}보다 큽니다.".format(b, a))
if a == b:
    print("입력했던 {} 와 {}는 같습니다.".format(a, b))
    