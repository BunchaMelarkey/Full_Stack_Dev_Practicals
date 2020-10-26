def countEven(start,limit):
	print("Numbers from {} to {}".format(start,limit-1))
	for number in range(start,limit):
		if number%2==0:
			print(str(number) + " (even number)")
		else:
			print(number)
	print("-----")
countEven(7,31)		