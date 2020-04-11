amount_of_items = 19
output_list = []
for i in range(1, amount_of_items + 1):
    if i % 2 == 0:
        priority = 'secondary'
    elif i % 3 == 0:
        priority = 'meh'
    else:
        priority = 'important'
    output_list.append([i, priority])

sorted_by_priority_list = []
for i in output_list:
    if i[1] == 'important':
        sorted_by_priority_list.append(i[1])
for i in output_list:
    if i[1] == 'meh':
        sorted_by_priority_list.append(i[1])
for i in output_list:
    if i[1] == 'secondary':
        sorted_by_priority_list.append(i[1])

for i in sorted_by_priority_list:
    print(i)