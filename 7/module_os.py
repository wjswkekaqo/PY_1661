import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd)
print("현재 폴더의 내부 요소:", os.listdir())

#폴더를 만들고 제거합니다.(폴더가 비었을 때만 가능)
os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")#파일 이름 변경

os.remove("new.txt")

os.system("dir")