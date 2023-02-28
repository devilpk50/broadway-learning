#operatinos
#data type methods
#data type built in fuctions
S1 = {1,2,3}
S1.add(4)
print("using add",S1)
S1.update([4,5,6])
print("using update", S1)
S1.remove(4)
print("using remove", S1)
S1.discard(5)
print("using discard", S1)
S1.pop()
print("using pop", S1)

a={2,3,4,5,6}
b={4,5,6,7,8}
c= a.union(b)
print("using union", c)
d=a.intersection(b)
print("using intersection", d)

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b:
    ##print(a, " is greater than" ,b)
    print(f"{a} is the greatest")
elif b>c:
   ## print(b," is greater")
    print(f"{b} is the greatest")
else :
   ## print(c, " is greater")
    print(f"{c} is the greatest")