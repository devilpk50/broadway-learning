# names = ['Jon', 'Jane']
# name = iter(names)
# print(next(name))
# print(next(name))
# print(next(name))

# language = 'java'
# lang = iter(language)

# print(next(lang))
# print(next(lang))
# print(next(lang))
# print(next(lang))
# print(next(lang))



#doing for loop using while loop

names = ['Jon', 'Jane']
name_iter = iter(names)
while True:
    try:
        name = next(name_iter)
        print(name)
    except StopIteration:
        break

