list_test = [1, 2, 1, 2, 3, 5, 6, 7, 8, 2, 4, 1, 5, 2]
value = 3

while value in list_test:
    list_test.remove(value)
    
print(list_test)