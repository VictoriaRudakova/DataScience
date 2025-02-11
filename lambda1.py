def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'was', 'name', 'he']

print(list(map(is_a_in_string,string_list)))