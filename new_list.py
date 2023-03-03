

def repeated_items(a):
    result = []
    for i in a:
        if a.count(i) > 1 and i not in result:
            result.append(i)
    return result

r = repeated_items([3,4,2,2,1,3,3,3])
print(r)