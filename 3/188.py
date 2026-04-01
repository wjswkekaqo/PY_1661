import datetime
now = datetime.datetime.now()
str_input = input("입력 ")
if str_input == "안녕":
    print("안녕하세요.")
elif str_input == "안녕하세요":
    print("안녕하세요.")
elif str_input == "지금 몇 시야?":
    print("지금은 {now}시입니다." .format(now=now.hour))
elif str_input == "지금 몇 시예요?":
    print("지금은 {now}시입니다." .format(now=now.hour))
else:
    print("잘지내?")
