import datetime

print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년",
      now.month, "월",
      now.day, "일",
      now.hour, "시",
      now.minute, "분",
      now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour\
    now.minute\
    now.second) 