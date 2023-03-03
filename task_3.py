def number_from_digits(a):
    number = 0
    for i in a:
        number = number * 10 + i
    return number

a = [1, 2, 3, 4, 5, 6 , 7]
result = number_from_digits(a)
print(result)