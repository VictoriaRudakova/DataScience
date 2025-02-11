#lambda expression

# def cube(number):
#     return number ** 3
#
# def cube(number):
#     return number ** 3
#
# number_list = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(cube,number_list)))



number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda number: number ** 3,number_list)))

print(list(filter(lambda number: number % 2 == 1, number_list)))

