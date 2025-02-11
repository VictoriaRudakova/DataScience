# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
# hello_with_kwargs(gender='female', age=21,name="Vik")
# hello_with_kwargs(gender='female', age=21)


# def hello_with_greeting_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(greeting,kwargs['name']))
#     else:
#         print('Hello! What is your name?'.format(greeting))
# hello_with_greeting_kwargs('Hello', gender='female', age=21,name="Vik")
# # hello_with_greeting_kwargs('Hi', gender='female', age=21)


def func_args_and_kwargs(*args, **kwargs):
    print('I would like {}, {}'.format(args[0], kwargs['food']))

func_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')