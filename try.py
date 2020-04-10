options = []
for i in range(1, 11):
    if i % 2 == 0:
        priority = 'secondary'
    else:
        priority = 'meh'
    options.append([i, priority])

for i in options:
    print(i)


test_list_of_id_1 = [x for x in range(1, 11)]
print(test_list_of_id_1)
test_list_of_id_2 = test_list_of_id_1[::-1]
print(test_list_of_id_2)
