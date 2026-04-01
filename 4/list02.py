insert_index = input("삽입할 인덱스를 입력하세요: ")
insert_value = input("삽입할 값을 입력하세요: ")
insert_index = int(insert_index)
insert_value = int(insert_value)

list_a= [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.extend([4, 5, 6])
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(insert_index, insert_value)
print(list_a)