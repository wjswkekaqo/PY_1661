import os

def read_forder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_forder(path+"/"+item)
        else:
            print("파일:", item)
        
read_forder(".")