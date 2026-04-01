number = input("숫자를 입력하세요: ")
try:
    number = float(number)
except ValueError:
    print("숫자가 아닙니다. 프로그램을 종료합니다.")
    exit()

if number > 0:
    print("양수입니다.")
if number < 0:
    print("음수입니다.")
if number == 0:
    print("영입니다.")
