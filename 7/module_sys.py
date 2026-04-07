import sys

print(sys.argv) #명령 매개변수 출력
print("---")

#컴퓨터 환경과 관련된 정보를 출력
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

sys.exit()#프로그램 강제 종료