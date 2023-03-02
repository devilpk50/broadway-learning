#wap to delete all the occurences of a specified character in a given string
# s="All the occurences of a specified character in a given string"
# input ="a"
#output:
#traversing

s="All the occurences of a specified character in a given string"
b =(input("enter to remove word:"))
for i in s:
    if b.lower() == i.lower():
        continue
    else:
        print(i, end="")

#  code by sir
# s="All the occurences of a specified character in a given string"
# b =input("enter to remove word:")
# result=""
# for each in s:
#     if each.lower() == b.lower():
#         continue
#     result = result + each

# print(result)