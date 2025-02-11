# def ten_percent_od_product(x,y,z):
#     return (x*y*z) * 0.1
#
# print(ten_percent_od_product(10, 20, 7))
#

# def ten_percent_od_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
# print(ten_percent_od_product_with_args(10, 20, 2, 1, 4, 345,458))

# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
# print(percent_of_product_with_args(40, 20, 2, 1, 4))


def func_with_kwargs(**kwargs):
    print(kwargs)

func_with_kwargs(first=1, second=2, third=3)


def func_with_args(*args):
    print(args)

func_with_args(1, 2, 3)

