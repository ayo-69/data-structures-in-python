my_array = [7, 12, 9, 4, 11]

lowest_value = my_array[0]

for i in my_array:
    if lowest_value > i:
        lowest_value = i

print(lowest_value)