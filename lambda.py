def sum_of_two_numbers(x):
    return x+x

number_list = [1, 2, 3, 4, 5, 6, 7]
result = map(sum_of_two_numbers, number_list)
print(result)

# for item in result:
#     print(item)

for item in map(sum_of_two_numbers, number_list):
    print(item)

print(list(map(sum_of_two_numbers,number_list)))