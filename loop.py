for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(0, 11):
    if(i%2==0):
        print(i,"is even no.")
   ## else:
      ##  print(i,"is odd no.") 

for i in range(1, 31):
    if i%3==0 and i%5==0:
        print("fizzbuzz", end="")
        break
    elif i%5==0:
        print("Buzz", end="")
    elif i%3==0:
        print("fizz", end="")
    else:
        print(i, end="")
       
#for x in [1,2,'a']:
   # print(x)

for x in "hey":
    print(x)
    