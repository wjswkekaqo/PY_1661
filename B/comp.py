#리스트 내포
a = [
    item * item
    for item in range(0, 10)
    if item % 2 == 0
]
#세트 내포
b = {
    item * item
    for item in range(0, 10)
    if item % 2 == 0
}
#딕셔너리 내포
c = {
    f"키_{item}":item * item
    for item in range(0, 10)
    if item % 2 == 0
}
#제너레이터 표현식
d = (
    item * item
    for item in range(0, 10)
    if item % 2 == 0
)


print(a)
print()
print(type(b), b)
print()
print(c)
print()
print(d)
