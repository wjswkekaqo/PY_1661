
try:
    score = float(input("학점 입력: "))
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")
else:
    if score >= 4.5:
     print("신")
    elif score >= 4.2:
        print("교수님의 사랑")
    elif score >= 3.5:
        print("현 체제의 수호자")
    elif score >= 2.8:
        print("일반인")
    elif score >= 2.3:
        print("일탈을 꿈꾸는 소시민")
    elif score >= 1.75:
        print("불가촉천민")
    elif score >= 1.0:
        print("자벌레")
    elif score >= 0.5:
        print("플랑크톤")
    elif score >= 0.0:
        print("시대를 앞서나는 혁명의 씨앗")
    else: 4.5 < score or score < 0.0
    print("잘못된 학점입니다.")
