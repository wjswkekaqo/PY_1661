i = 0
while True:
    i = i + 1
    print("{}번째 반복분입니다.".format(i))
    input_text = input(">종료하시겠습니까?(y/n): ")
    if input_text in ["y"]:
        print("반복을 종료합니다.")
        break