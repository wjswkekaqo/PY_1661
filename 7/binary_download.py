from urllib import request

target = request.urlopen("https://www.python.org/static/img/python-logo.png")
output = target.read()
print(output)

file = open("output.png", "wb")
file.write(output)
file.close()