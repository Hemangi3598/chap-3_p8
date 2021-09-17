# wapp to find the sum of the digits
# i/p : 354 o/p = 12

num = int(input("enter the number")) 
if num < 0:
	print("invalid number")
else:
	sum = 0
	while num > 0:
		digit = num % 10                     # get the last digit
		sum =  sum + digit                      # use the last digit
		num =  num // 10                      # remove the last digit
	print("sum = ", sum)