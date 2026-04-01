dictionary = {
    "name": "7D  건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "8D  건조 망고"
print("name:", dictionary["name"])
#dictionary[새로운 키] = 새로운 값
#del dictionary[키] : 키와 값을 삭제