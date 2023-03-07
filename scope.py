# a = 1

# def summ(b, c):
#     global a
#     a = 2
#     print("Inside Function", a)
#     return b + c

# print("Outside Function", a)
# #print(summ(2, 3))
# summ(2, 3)
# print("outside function", a)


# def summ(*args):
#     print(args)
#     print(type(args))
#     return sum(args)


# print(summ(1))
# print(summ(1, 2))
# summ(1, 2, 3)
# summ(1, 2, 3, 4)
# summ(1, 2, 3, 4, 5)


def summ(**kwargs):
    print(kwargs)
    print(type(kwargs))

print(summ(a=1))
print(summ(a=1, b=2))
print(summ(a=1, b=2, c=3))