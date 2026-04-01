number = input("정수 입력>")
number = int(number)

if number > 0:
    raise NotImplementedError("양수는 아직 구현되지 않았습니다.")
else:
    raise NotImplementedError("음수는 아직 구현되지 않았습니다.")
# IndentationError 들여쓰기가 잘못되어 있다.
# pass는 아무것도 하지 않는 명령어로, 조건문에서 실행할 코드가 없을 때 사용한다.