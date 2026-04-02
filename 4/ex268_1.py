a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
count = {}
for i in a:
    if i not in count:
        count[i] = 0
        count[i] += 1
        
print(f"{a}에서")
print(f"사용된 숫자의 종류는 {len(count)}개입니다.")