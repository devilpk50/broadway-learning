

# # def summ(a, b):
# #     return a + b

# # print(summ(5, 4))

# def decorator_me(func):
#     def inner_func(*args, **kwargs):
#     # def inner_func(a, b):
#         print('it is a decorative function')
#         return func(*args, **kwargs)
#     return inner_func


#         # print(f"total function execution time is {end-start}")
       

# @decorator_me
# def addition(a, b, c):
#     return a + b + c

# # r = decorator_me(addition)
# print(addition(3, 4, 6))

# # import time
# # start = time.time()
# # print(addition(3, 4, 11))
# # end = time.time()
# # print(f"total function execution time is {end - start}")
import time

def execution_time(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        r= func(*args, **kwargs)
        end = time.time()
        print(f"total function execution time is {end - start}")
        return r
    return inner_func

@execution_time
def message_print():
    time.sleep(5)
    # for i in range(100000000):
    #     pass
    print("Hello World")


# message = execution_time(message_print)
message_print()
