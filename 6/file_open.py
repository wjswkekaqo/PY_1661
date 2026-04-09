#file = open("basic.txt", "w")
#file.write("hello python programming...!")
#file.close()

with open("basic.txt", "w", encoding="utf-8") as file:
    file.write("hello python programming....!")
