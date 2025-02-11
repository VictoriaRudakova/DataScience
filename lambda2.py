# filter()

def is_number_odd(number):
    return number % 2 == 1

number_list = [1, 2, 3, 4, 5, 6, 7]


print(filter(is_number_odd, number_list))

print(list(filter(is_number_odd, number_list)))


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'was', 'name', 'he']

print(list(filter(is_a_in_string,string_list)))