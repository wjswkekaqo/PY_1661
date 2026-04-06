def write_text_file(filename, text):
    try:
        file = open(filename, "w")#파일 열기
        
        return
    
        file.write(text)
        
    except:
        print("오류가 발생했습니다.")
        
    finally:
        file.close()#파일 닫기

write_text_file("test.txt", "안녕하세요!")