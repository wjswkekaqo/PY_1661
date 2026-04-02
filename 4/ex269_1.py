dna = input("염기 서열을 입력해주세요: ").lower()
count = {
    "a" : 0,
    "t" : 0,
    "g" : 0,
    "c" : 0
}
for i in dna:
    if i in count:
        count[i] +=1
for key in count:
    print(f"{key}의 개수: {count[key]}") 