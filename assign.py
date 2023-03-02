# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2 

# print(difference(22))
# print(difference(14))

# Number to be checked for prime

n = 5
if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
# If the number is less than 1, its also not a prime number.
else:
	print(n, "is not a prime number")

