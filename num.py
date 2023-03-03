# a = [54, 2, 99, 3, 20, 1]
def custom_sort(a):  #bubble sort
    length = len(a)

    for i in range(length - 1):
        for j in range(i+1, length):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a

a = [54, 1, 99, 20, 3]
b = [1, 5, 0, 100, 20]
result = custom_sort(a)
resu= custom_sort(b)
print(result)
print(resu)
