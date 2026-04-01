number = input("정수 입력: ")

last_char = number[-1]
last_number = int(last_char)
if last_number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
if last_number == 0:
    print("0입니다.")