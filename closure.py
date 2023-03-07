# def func(name):
#     return 'Hello' + name.upper() + '.'

# def greet(my_func):
#     message = my_func('Jane')
#     print(message)

# greet(func)


def greet(msg):
    def print_message():
        print(msg)
    return print_message

message = greet("Hello World")
message()