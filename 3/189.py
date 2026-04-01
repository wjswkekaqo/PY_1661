int_input = input("정수를 입력해주세요: ")
int_input = int(int_input)

if int_input % 2 != 0:
    print("2로 나누어 떨어지는 숫자가 아닙니다.")
if int_input % 3 == 0:
    print("3으로 나누어 떨어지는 숫자입니다.")
if int_input % 4 != 0:
    print("4로 나누어 떨어지는 숫자가 아닙니다.")
if int_input % 5 != 0:
    print("5로 나누어 떨어지는 숫자가 아닙니다.")
